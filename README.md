# Lista 09 — Jogo do Puzzle de 8 Peças

## Objetivo

Desenvolver o **Jogo do Puzzle de 8 peças (8-Puzzle)** utilizando pelo menos **três métodos de busca** entre os estudados, sendo **A**\* obrigatório com **duas heurísticas diferentes**. O projeto inclui:

- Implementação do jogo com interface gráfica;
- Aplicação de algoritmos de busca:
  - Busca em Largura (BFS)
  - Busca em Profundidade (DFS)
  - Busca Uniforme (UCS)
  - Busca Gulosa
  - Busca A\* (com duas heurísticas)
- Relatório comparativo detalhado entre os métodos e heurísticas.


## Métodos de Busca Implementados

* **Busca em Largura (BFS)**: percorre os estados do jogo em largura, expandindo os nós mais próximos da raiz.
* **Busca em Profundidade (DFS)**: explora o caminho mais profundo primeiro, podendo ser ineficiente sem controle de profundidade.
* **Busca Uniforme (UCS)**: variação da BFS com custo de caminho acumulado.
* **Busca Gulosa (Greedy)**: utiliza apenas a heurística para decidir o próximo estado.
* **A\***: combina custo acumulado e heurística (f(n) = g(n) + h(n)), testado com **duas heurísticas diferentes**.


## Heurísticas utilizadas no A\* e na Busca Gulosa

1. **Número de peças fora do lugar** (h1): simples e rápida.
2. **Distância de Manhattan** (h2): soma das distâncias horizontais e verticais de cada peça à sua posição correta.


## Relatório

O relatório anexo apresenta:

* Descrição de cada algoritmo e heurística;
* Comparação dos métodos usando os mesmos estados iniciais;
* Tempo de execução;
* Eficiência e escalabilidade de cada abordagem;
* Considerações sobre melhor desempenho.


## Tecnologias utilizadas

* **Linguagem**: Python
* **Interface gráfica**: Tkinter


## Estrutura do Projeto

```
8puzzle/
│
├── main.py
├── puzzle/
│   ├── __init__.py
│   ├── state.py
│   ├── actions.py
│   ├── heuristics.py
│   └── algorithms.py
├── search/
│   ├── __init__.py
│   ├── bfs.py
│   ├── dfs.py
│   ├── ucs.py
│   ├── greedy.py
│   └── astar.py
├── heuristics/
│   ├── __init__.py
│   ├── misplaced.py
│   └── manhattan.py
├── gui/
│   └── __init__.py
│   └── app.py
├── utils/
│   └── __init__.py
│   └── util.py
├── tests/
├── ├── tests.py
├── ├── state_test_gui.txt
├── └── data/
├──     ├── Easy.txt
├──     ├── Medium.txt
├──     └── Hard.txt
├── relatório.pdf
└── README.md
```
