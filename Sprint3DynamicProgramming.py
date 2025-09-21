from collections import deque

# ------------------------------
# Produtos disponíveis
# ------------------------------
produtos = [
    "reagente_X", "luvas", "máscaras", "seringas", "algodão",
    "tubos_coleta", "etiquetas", "álcool_gel", "gazes", "papel_laboratorio"
]

# ------------------------------
# Fila e Pilha usando listas
# ------------------------------
fila_consumo = []  # ordem cronológica
consumo_total = {p: 0 for p in produtos}  # soma total do consumo por produto

# ------------------------------
# Registrar consumo manual
# ------------------------------
def registrar_consumo_manual():
    print("\n=== Registrar Consumo Diário ===")
    produto = escolher_produto()
    try:
        quantidade = int(input(f"Quantidade consumida de {produto}: "))
        # Adiciona ao final da lista (fila)
        fila_consumo.append([produto, quantidade])
        consumo_total[produto] += quantidade
        print(f"✅ Consumo registrado: {produto} - {quantidade}")
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

# ------------------------------
# Exibir Fila (FIFO)
# ------------------------------
def mostrar_fila():
    print("\n=== Consumo em ordem cronológica (Fila) ===")
    if not fila_consumo:
        print("Nenhum consumo registrado ainda.")
    else:
        for i in range(len(fila_consumo)):
            produto, qtd = fila_consumo[i]
            print(f"{i+1}. {produto} - {qtd}")

# ------------------------------
# Exibir Pilha (LIFO)
# ------------------------------
def mostrar_pilha():
    print("\n=== Consumo em ordem inversa (Pilha) ===")
    if not fila_consumo:
        print("Nenhum consumo registrado ainda.")
    else:
        for i in range(len(fila_consumo)-1, -1, -1):
            produto, qtd = fila_consumo[i]
            print(f"{len(fila_consumo)-i}. {produto} - {qtd}")

# ------------------------------
# Escolher produto
# ------------------------------
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

# ------------------------------
# Buscas
# ------------------------------
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

# ------------------------------
# Ordenação por consumo total (descendente)
# ------------------------------
def merge_sort(lista, consumo_total):
    if len(lista) <= 1:
        return lista[:]
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
        return lista[:]
    pivot = lista[0]
    menores = [x for x in lista[1:] if consumo_total[x] >= consumo_total[pivot]]
    maiores = [x for x in lista[1:] if consumo_total[x] < consumo_total[pivot]]
    return quick_sort(menores, consumo_total) + [pivot] + quick_sort(maiores, consumo_total)

# ------------------------------
# Menu principal
# ------------------------------
def menu():
    while True:
        print("\n--- Menu ---")
        print("1 - Registrar consumo diário (Fila)")
        print("2 - Ver consumo em ordem cronológica (Fila)")
        print("3 - Ver consumo em ordem inversa (Pilha)")
        print("4 - Busca sequencial por produto")
        print("5 - Busca binária por produto")
        print("6 - Produtos ordenados por consumo total (merge sort)")
        print("7 - Produtos ordenados por consumo total (quick sort)")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar_consumo_manual()
        elif opcao == "2":
            mostrar_fila()
        elif opcao == "3":
            mostrar_pilha()
        elif opcao == "4":
            produto_alvo = escolher_produto()
            idx = busca_sequencial(produto_alvo)
            if idx != -1:
                print(f"Produto '{produto_alvo}' encontrado na posição {idx} na lista de produtos.")
            else:
                print(f"Produto '{produto_alvo}' não encontrado.")
        elif opcao == "5":
            produto_alvo = escolher_produto()
            idx = busca_binaria(produto_alvo)
            if idx != -1:
                print(f"Produto '{produto_alvo}' encontrado na lista ordenada de produtos na posição {idx}.")
            else:
                print(f"Produto '{produto_alvo}' não encontrado.")
        elif opcao == "6":
            ordenados_merge = merge_sort(produtos[:], consumo_total)
            print("\nProdutos ordenados por consumo total (merge sort):")
            for p in ordenados_merge:
                print(f"{p} - Consumo total: {consumo_total[p]}")
        elif opcao == "7":
            ordenados_quick = quick_sort(produtos[:], consumo_total)
            print("\nProdutos ordenados por consumo total (quick sort):")
            for p in ordenados_quick:
                print(f"{p} - Consumo total: {consumo_total[p]}")
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

# ------------------------------
# Inicialização
# ------------------------------
if __name__ == "__main__":
    menu()
