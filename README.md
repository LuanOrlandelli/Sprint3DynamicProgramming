# Documentação do Sistema de Controle de Estoque Hospitalar

Este documento explica os dois códigos do projeto, mostrando como cada estrutura de dados e algoritmo foi aplicado para atender aos requisitos do sistema.

Há dois códigos pois um segue os requisitos propostos na Sprint, e o outro segue a ideia central do projeto (que gera aleatóriamente os dados, os analisa e faz previsões)

---
## Integrantes

* Arthur Bobadilla Franchi – RM555056
* Luan Orlandelli Ramos – RM554747
* Arthur Albuquerque Menezes – RM562950
* Caio Rasuck Barbosa – RM93645
* Jorge Luiz – RM554418

**Turma:** 2ESPY

---

## 1. Código "Sprint 3 Dynamic Programming"

### Descrição Geral

Este código permite registrar o consumo diário de insumos manualmente, usando listas para simular **fila** e **pilha**. Também implementa **buscas** (sequencial e binária) e **algoritmos de ordenação** (Merge Sort e Quick Sort) para análise dos dados.

### Estruturas de Dados

* **Lista `fila_consumo`**: simula a fila (FIFO). Os consumos são adicionados ao final da lista e exibidos do início ao fim.
* **Pilha (LIFO)**: exibida percorrendo a lista do final para o início, simulando comportamento de pilha.
* **Dicionário `consumo_total`**: armazena a soma total de consumo de cada produto, usado nas ordenações.

### Funções e Algoritmos

* **`registrar_consumo_manual()`**: solicita ao usuário o produto e a quantidade consumida. Adiciona o registro na fila e atualiza o consumo total.
* **`mostrar_fila()`**: exibe os consumos na ordem cronológica (FIFO).
* **`mostrar_pilha()`**: exibe os consumos em ordem inversa (LIFO).
* **`busca_sequencial(produto)`**: percorre a lista de produtos para localizar o produto alvo.
* **`busca_binaria(produto)`**: busca eficiente em lista ordenada de produtos.
* **`merge_sort(lista, consumo_total)`** e **`quick_sort(lista, consumo_total)`**: ordenam os produtos com base no consumo total, do maior para o menor.

### Menu

O menu permite ao usuário:

1. Registrar consumo diário
2. Ver consumo em ordem cronológica (fila)
3. Ver consumo em ordem inversa (pilha)
4. Buscar produto (sequencial)
5. Buscar produto (binária)
6. Ordenar produtos por consumo total (merge sort)
7. Ordenar produtos por consumo total (quick sort)
8. Sair

---

## 2. Código "main"

### Descrição Geral

Este código simula o estoque de insumos hospitalares, registra consumo aleatório e calcula previsões de compra para os próximos 7 dias. Ele também oferece análises sobre produtos em falta, sobrando e tempo até zerar estoque.

### Estruturas de Dados

* **Listas `produtos` e `unidades`**: armazenam os produtos disponíveis e unidades hospitalares.
* **Dicionário `valores_unitarios`**: armazena o valor unitário de cada produto.
* **Dicionário `consumo_diario`**: armazena o consumo diário dos últimos 7 dias para cada produto.
* **Dicionário `estoque`**: armazena o estoque atual e ideal de cada produto por unidade.
* **Dicionários `faltantes` e `sobrando`**: armazenam produtos que estão abaixo ou acima do estoque ideal.
* **Função recursiva `dias_para_zerar`**: calcula quantos dias levará para o estoque zerar baseado no consumo passado.

### Funções e Algoritmos

* **`gerar_consumo_aleatorio()`**: cria dados de consumo para 7 dias de cada produto.
* **`gerar_estoque_aleatorio()`**: cria dados de estoque ideal e atual para cada unidade e produto.
* **`produtos_em_falta()` e `produtos_sobrando()`**: identificam produtos fora do estoque ideal.
* **`previsao_compra()`**: calcula a quantidade recomendada para compra baseado no consumo passado e estoque atual.
* **`busca_sequencial()` e `busca_binaria()`**: localizam produtos.
* **`merge_sort()` e `quick_sort()`**: ordenam produtos pelo consumo total.
* **Funções de exibição**: mostram estoque, consumo diário, produtos em falta/sobrando, dias até zerar e previsão de compra.

### Menu

O menu permite ao usuário acessar todas as análises, incluindo:

1. Ver estoque
2. Ver consumo diário dos últimos 7 dias
3. Busca sequencial por produto
4. Busca binária por produto
5. Ordenar produtos por consumo total (merge sort)
6. Ordenar produtos por consumo total (quick sort)
7. Produtos em falta e sobrando
8. Dias até zerar os produtos
9. Previsão de compra para os próximos 7 dias
10. Relatório completo
11. Sair

---

### Observações Finais

* O **primeiro código** atende especificamente aos requisitos de **fila e pilha**, mantendo buscas e ordenações.
* O **segundo código** é mais completo, simulando todo o sistema de estoque e previsões.

---

Fim da documentação.
