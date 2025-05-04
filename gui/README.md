# Interface Gráfica - GUI

## Barra de Navegação

A barra de navegação deve conter os seguintes botões:

  - [X] Botão para escolher o algoritmo (bfs, dfs, a*, greedy, ucs)
  - [X] Botão para escolher a heurística (manhattan, misplaced, nenhuma)
  - [X] Botão para escolher o estado inicial (de um arquivo)
  - [X] Botão para gerar aleatóriamente o estado inicial
  - [X] Botão para resolver o puzzle (deve chamar a função solve do puzzle.py)
  - [X] Botão para reiniciar o jogo (deve chamar a função reset do puzzle.py)
  - [X] Botão para sair do jogo (deve chamar a função exit do puzzle.py)

## Principal

No centro da tela deve ter os seguintes elementos:

  - [X] título (deve ser o nome do jogo)
  - [X] tabuleiro (deve ser uma grade de botões, cada botão deve representar uma peça do puzzle)
  - [X] contador de passos (deve mostrar o número de passos dados para resolver o puzzle)
  - [X] contador de tempo (deve mostrar o tempo gasto para resolver o puzzle)

## Funcionalidades:

  - [X] O usuário escolhe o algoritmo e a heurística na navbar
  - [X] O usuário escolhe o estado inicial na navbar ou gera aleatóriamente
  - [X] O usuário clica no botão resolver e o jogo começa a rodar
  - [X] O usuário pode ver o tabuleiro sendo atualizado a cada passo
  - [X] O usuário pode ver o contador de passos e o contador de tempo sendo atualizados a cada passo
  - [X] O usuário pode reiniciar o jogo a qualquer momento
  - [X] O usuário pode sair do jogo a qualquer momento
  - [X] O usuário pode escolher outro algoritmo e heurística a qualquer momento
  - [X] O usuário pode escolher outro estado inicial e final a qualquer momento
  - [X] O usuário pode gerar aleatóriamente o estado inicial a qualquer momento

## Detalhes

- [X] Mostrar um tela de erro, caso gere alguma exceção no código
- [X] Deixar tamanho da janela fixo em 900x500 e não pode ser alterado
