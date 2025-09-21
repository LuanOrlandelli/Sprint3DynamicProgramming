# Integrantes do grupo – só pra deixar registrado mesmo.
# Arthur Bobadilla Franchi - RM555056
# Luan Orlandelli Ramos - RM554747
# Arthur Albuquerque Menezes - RM562950
# Caio Rasuck Barbosa - RM93645
# Jorge Luiz - RM554418

import random
from functools import lru_cache

# Produtos e valores unitários fixos
produtos = [
    "reagente_X", "luvas", "máscaras", "seringas", "algodão",
    "tubos_coleta", "etiquetas", "álcool_gel", "gazes", "papel_laboratorio"
]

valores_unitarios = {
    "reagente_X": 15.0,
    "luvas": 0.50,
    "máscaras": 1.20,
    "seringas": 0.80,
    "algodão": 0.10,
    "tubos_coleta": 2.00,
    "etiquetas": 0.05,
    "álcool_gel": 7.00,
    "gazes": 0.30,
    "papel_laboratorio": 3.00
}

unidades = ["Unidade_A", "Unidade_B"]

def gerar_consumo_aleatorio():
    consumo = {}
    for produto in produtos:
        consumo[produto] = [random.randint(1, 30) for _ in range(7)]
    return consumo

def gerar_estoque_aleatorio():
    estoque = {}
    for unidade in unidades:
        estoque[unidade] = {}
        for produto in produtos:
            ideal = random.randint(50, 200)
            if random.random() < 0.5:
                atual = random.randint(int(ideal * 1.1), int(ideal * 1.8))
            else:
                atual = random.randint(int(ideal * 0.8), ideal)
            valor_unitario = valores_unitarios[produto]
            estoque[unidade][produto] = {
                "ideal": ideal,
                "atual": atual,
                "valor_unitario": valor_unitario
            }
    return estoque

def produtos_em_falta(estoque):
    faltantes = {}
    for unidade, produtos_estoque in estoque.items():
        faltantes[unidade] = [
            p for p, d in produtos_estoque.items() if d["atual"] < d["ideal"]
        ]
    return faltantes

def produtos_sobrando(estoque):
    sobrando = {}
    for unidade, produtos_estoque in estoque.items():
        sobrando[unidade] = [
            p for p, d in produtos_estoque.items() if d["atual"] > d["ideal"]
        ]
    return sobrando

@lru_cache(maxsize=None)
def dias_para_zerar(produto, quantidade_atual, dia=0):
    if quantidade_atual <= 0:
        return 0
    consumo = consumo_diario[produto]
    if dia >= len(consumo):
        media = sum(consumo) / len(consumo)
        return 1 + dias_para_zerar(produto, quantidade_atual - media, dia)
    else:
        return 1 + dias_para_zerar(produto, quantidade_atual - consumo[dia], dia + 1)

def previsao_compra(estoque, consumo_diario, dias_previsao=7):
    previsoes = {}
    for unidade, produtos_estoque in estoque.items():
        previsoes[unidade] = {}
        for produto, dados in produtos_estoque.items():
            estoque_atual = dados["atual"]
            estoque_ideal = dados["ideal"]
            consumo_passado = consumo_diario[produto]
            consumo_medio = sum(consumo_passado) / len(consumo_passado)
            consumo_futuro = consumo_medio * dias_previsao
            total_necessario = estoque_ideal + consumo_futuro
            compra = total_necessario - estoque_atual
            compra = max(0, round(compra))
            previsoes[unidade][produto] = {
                "estoque_atual": estoque_atual,
                "consumo_passado_7d": sum(consumo_passado),
                "consumo_medio_diario": round(consumo_medio, 2),
                "compra_recomendada": compra
            }
    return previsoes

def busca_sequencial(produto_alvo):
    for i, p in enumerate(produtos):
        if p == produto_alvo:
            return i
    return -1

def busca_binaria(produto_alvo):
    lista_ordenada = sorted(produtos)
    left, right = 0, len(lista_ordenada) - 1
    while left <= right:
        mid = (left + right) // 2
        if lista_ordenada[mid] == produto_alvo:
            return mid
        elif lista_ordenada[mid] < produto_alvo:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def merge_sort(lista, consumo_total):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio], consumo_total)
    direita = merge_sort(lista[meio:], consumo_total)
    return merge(esquerda, direita, consumo_total)

def merge(esquerda, direita, consumo_total):
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if consumo_total[esquerda[i]] >= consumo_total[direita[j]]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

def quick_sort(lista, consumo_total):
    if len(lista) <= 1:
        return lista
    pivot = lista[0]
    menores = [x for x in lista[1:] if consumo_total[x] >= consumo_total[pivot]]
    maiores = [x for x in lista[1:] if consumo_total[x] < consumo_total[pivot]]
    return quick_sort(menores, consumo_total) + [pivot] + quick_sort(maiores, consumo_total)

def mostrar_estoque():
    print("\n=== Estoque ===")
    for unidade, produtos_estoque in estoque.items():
        print(f"\n{unidade}:")
        for produto, dados in produtos_estoque.items():
            print(f"  {produto}: atual={dados['atual']} ideal={dados['ideal']} valor_unitario={dados['valor_unitario']}")

def mostrar_consumo_diario():
    print("\n=== Consumo diário dos últimos 7 dias ===")
    for produto, consumos in consumo_diario.items():
        print(f"  {produto}: {consumos}")

def mostrar_produtos_em_falta_e_sobrando():
    faltantes = produtos_em_falta(estoque)
    sobrando = produtos_sobrando(estoque)
    print("\n=== Produtos em falta ===")
    for unidade, itens in faltantes.items():
        print(f"{unidade}: {', '.join(itens) if itens else 'Nenhum'}")
    print("\n=== Produtos sobrando ===")
    for unidade, itens in sobrando.items():
        print(f"{unidade}: {', '.join(itens) if itens else 'Nenhum'}")

def mostrar_dias_ate_zerar():
    dias_ate_zerar = {
        unidade: {
            produto: dias_para_zerar(produto, dados["atual"])
            for produto, dados in produtos_estoque.items()
        }
        for unidade, produtos_estoque in estoque.items()
    }
    print("\n=== Dias até zerar estoque ===")
    for unidade, produtos in dias_ate_zerar.items():
        print(f"\n{unidade}:")
        for produto, dias in produtos.items():
            print(f"  {produto}: {dias:.0f} dias")

def mostrar_previsao_compra():
    previsoes = previsao_compra(estoque, consumo_diario)
    print("\n=== Previsão de compra para os próximos 7 dias ===")
    for unidade, produtos_prev in previsoes.items():
        print(f"\n{unidade}:")
        for produto, dados in produtos_prev.items():
            print(f"  {produto}:")
            print(f"    Estoque atual: {dados['estoque_atual']}")
            print(f"    Consumo passado (7d): {dados['consumo_passado_7d']}")
            print(f"    Consumo médio diário: {dados['consumo_medio_diario']}")
            print(f"    Compra recomendada: {dados['compra_recomendada']}")

def mostrar_relatorio_completo():
    mostrar_estoque()
    mostrar_consumo_diario()
    mostrar_produtos_em_falta_e_sobrando()
    mostrar_dias_ate_zerar()
    mostrar_previsao_compra()

def escolher_produto():
    print("\nEscolha o produto pelo número:")
    for i, p in enumerate(produtos):
        print(f"{i + 1} - {p}")
    while True:
        try:
            escolha = int(input("Número do produto: "))
            if 1 <= escolha <= len(produtos):
                return produtos[escolha - 1]
            else:
                print("Número inválido, tente novamente.")
        except ValueError:
            print("Entrada inválida, digite um número.")

consumo_diario = gerar_consumo_aleatorio()
estoque = gerar_estoque_aleatorio()

def menu():
    while True:
        print("\n--- Menu ---")
        print("1 - Ver estoque")
        print("2 - Consumo diário dos últimos 7 dias")
        print("3 - Busca sequencial por produto")
        print("4 - Busca binária por produto")
        print("5 - Produtos ordenados por consumo total (merge sort)")
        print("6 - Produtos ordenados por consumo total (quick sort)")
        print("7 - Produtos em falta e sobrando")
        print("8 - Dias até zerar os produtos")
        print("9 - Previsão de compra para os próximos 7 dias")
        print("10 - Relatório completo")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_estoque()
        elif opcao == "2":
            mostrar_consumo_diario()
        elif opcao == "3":
            produto_alvo = escolher_produto()
            idx = busca_sequencial(produto_alvo)
            print(f"Produto '{produto_alvo}' encontrado na posição {idx} na lista de produtos.")
        elif opcao == "4":
            produto_alvo = escolher_produto()
            idx = busca_binaria(produto_alvo)
            if idx != -1:
                print(f"Produto '{produto_alvo}' encontrado na posição {idx} na lista ordenada de produtos.")
            else:
                print(f"Produto '{produto_alvo}' não encontrado.")
        elif opcao == "5":
            consumo_total = {p: sum(consumo_diario[p]) for p in produtos}
            ordenados_merge = merge_sort(produtos, consumo_total)
            print("\nProdutos ordenados por consumo total (merge sort):")
            for p in ordenados_merge:
                print(f"{p} - Consumo total: {consumo_total[p]}")
        elif opcao == "6":
            consumo_total = {p: sum(consumo_diario[p]) for p in produtos}
            ordenados_quick = quick_sort(produtos, consumo_total)
            print("\nProdutos ordenados por consumo total (quick sort):")
            for p in ordenados_quick:
                print(f"{p} - Consumo total: {consumo_total[p]}")
        elif opcao == "7":
            mostrar_produtos_em_falta_e_sobrando()
        elif opcao == "8":
            mostrar_dias_ate_zerar()
        elif opcao == "9":
            mostrar_previsao_compra()
        elif opcao == "10":
            mostrar_relatorio_completo()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
