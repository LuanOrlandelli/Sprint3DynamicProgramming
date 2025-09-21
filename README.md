
# Controle de Estoque Hospitalar – Projeto

## 1. Código de Consumo Manual com Fila, Pilha, Buscas e Ordenação

Este código simula o registro de consumo diário de insumos hospitalares, permitindo a análise tanto cronológica quanto inversa, além de buscas e ordenação por consumo total.

### Produtos
```python
produtos = [
    "reagente_X", "luvas", "máscaras", "seringas", "algodão",
    "tubos_coleta", "etiquetas", "álcool_gel", "gazes", "papel_laboratorio"
]
```
Lista fixa de produtos utilizados nas unidades.

### Estruturas de Dados

#### Fila (FIFO)
- Implementada com `deque` do Python:
```python
fila_consumo = deque()
```
- Armazena o consumo diário em ordem cronológica. Cada registro é uma tupla `(produto, quantidade)`.
- Permite simular o registro do consumo conforme ele ocorre ao longo do tempo.

#### Pilha (LIFO)
- Implementada de forma indireta usando `reversed` sobre a fila:
```python
for i, (produto, qtd) in enumerate(reversed(list(fila_consumo)), 1):
```
- Permite consultar os últimos consumos primeiro, simulando verificações recentes de estoque.

### Registro de Consumo Manual
- O usuário insere manualmente a quantidade consumida de cada insumo.
- Atualiza tanto a fila quanto um dicionário `consumo_total` para armazenamento agregado.

### Estruturas de Busca
1. **Busca sequencial**
```python
def busca_sequencial(produto_alvo):
    for i, p in enumerate(produtos):
        if p == produto_alvo:
            return i
```
- Varre a lista de produtos do início ao fim.
- Útil para listas pequenas ou sem ordenação.

2. **Busca binária**
```python
def busca_binaria(produto_alvo):
    lista_ordenada = sorted(produtos)
```
- Requer lista ordenada.
- Divide a lista repetidamente até localizar o produto.
- Mais eficiente que a busca sequencial em listas grandes.

### Ordenação por Consumo Total
1. **Merge Sort**
```python
def merge_sort(lista, consumo_total):
```
- Ordena produtos por quantidade consumida de forma decrescente.
- Divide e conquista: divide a lista em sublistas, ordena e junta.

2. **Quick Sort**
```python
def quick_sort(lista, consumo_total):
```
- Ordena produtos de acordo com consumo total.
- Escolhe um pivô e separa em maiores e menores.
- Recursivamente combina para formar a lista ordenada.

### Menu
- Permite registrar consumos, visualizar fila/pilha, realizar buscas e ordenações.

---

## 2. Código de Previsão de Estoque com Relatórios

Este código complementa o anterior, simulando o estoque e o consumo de forma aleatória, mas mantendo conceitos de controle de estoque e previsão de compra.

### Estoque
- Cada unidade possui um estoque de produtos com `atual` e `ideal`.
```python
estoque[unidade][produto] = {
    "ideal": ideal,
    "atual": atual,
    "valor_unitario": valor_unitario
}
```

### Consumo Diário
- Armazenado em dicionário com listas de 7 dias:
```python
consumo_diario[produto] = [random.randint(1, 30) for _ in range(7)]
```
- Simula histórico de consumo para previsão.

### Previsão de Compra
- Calcula consumo médio dos últimos 7 dias.
- Estima o total necessário para manter estoque ideal + consumo futuro.
- Gera recomendação de compra por produto.

### Estruturas de Busca e Ordenação
- **Busca sequencial** e **busca binária** para localizar produtos.
- **Merge Sort** e **Quick Sort** para ordenar produtos por consumo total.
- Permite análise do consumo e priorização de reposição.

### Relatórios
1. **Estoque atual**
2. **Consumo diário**
3. **Produtos em falta ou sobrando**
4. **Dias até zerar o estoque** (`lru_cache` otimiza cálculos recursivos)
5. **Previsão de compra para 7 dias**

### Integração com Fila/Pilha
- Embora este código gere os dados aleatoriamente, ele pode ser adaptado para usar registros manuais em fila/pilha, unificando os dois sistemas.

---

## 3. Conclusão

- **Fila e Pilha:** simulam registro cronológico e consultas inversas de consumo, atendendo ao requisito de rastreabilidade.
- **Buscas:** permitem localizar rapidamente produtos em registros históricos ou relatórios.
- **Ordenação:** permite priorizar insumos mais consumidos para reposição.
- **Relatórios e previsões:** facilitam decisões de compra e controle de estoque hospitalar.
