from __future__ import annotations
import copy
from .actions import Actions
from typing import List, Tuple

class State:
    """
    Classe representando o estado do quebra-cabeça.
    Cada estado é representado por uma matriz 2D (lista de listas) que representa o
    tabuleiro do quebra-cabeça.
    """
    def __init__(self, board: List[List[int]]) -> None:
        self.board = board
        self.blank_tile = self.find_blank_tile()
    # __init__

    def __str__(self) -> str:
        """
        Representação em string do estado do quebra-cabeça.
        """
        return "\n".join(" ".join(str(tile) for tile in row) for row in self.board)
    # __str__

    def __eq__(self, other: State) -> bool:
        """
        Compara dois estados do quebra-cabeça.
        """
        return isinstance(other, State) and self.board == other.board
    # __eq__

    def __lt__(self, other):
        """
        Compara dois estados do quebra-cabeça.
        Isso é usado para ordenar os estados em uma fila de prioridade.
        """
        return self.board < other.board
    # __lt__

    def __hash__(self) -> int:
        """
        Gera um hash para o estado do quebra-cabeça.
        Isso é útil para armazenar estados em conjuntos ou dicionários.
        """
        return hash(tuple(tuple(row) for row in self.board))
    # __hash__

    def find_blank_tile(self) -> Tuple[int, int]:
        """
        Encontra a posição do espaço em branco (0) no tabuleiro.
        Retorna as coordenadas (linha, coluna) do espaço em branco.
        """
        for i, row in enumerate(self.board):
            for j, value in enumerate(row):
                if value == 0:
                    return i, j
        raise ValueError("No blank tile found in the board.")
    # find_blank_tile

    def move(self, action: Actions) -> State | None:
        """
        Move o espaço em branco (0) em uma direção especificada pela ação.
        Retorna um novo estado do quebra-cabeça após o movimento.
        Se o movimento não for válido, retorna None.
        """
        state = None
        blank_row, blank_col = self.blank_tile
        target_row, target_col = blank_row, blank_col

        if action == Actions.UP:
            target_row -= 1
        elif action == Actions.DOWN:
            target_row += 1
        elif action == Actions.LEFT:
            target_col -= 1
        elif action == Actions.RIGHT:
            target_col += 1
        elif action == Actions.NO_OP:
            state = self

        if 0 <= target_row < len(self.board) and 0 <= target_col < len(self.board[0]):
            new_board = copy.deepcopy(self.board)
            
            new_board[blank_row][blank_col], new_board[target_row][target_col] = new_board[target_row][target_col], new_board[blank_row][blank_col]

            state = State(new_board)

        return state
    # move

    def get_possible_moves(self) -> List[Actions]:
        """
        Retorna uma lista de ações possíveis a partir do estado atual do quebra-cabeça.
        As ações são determinadas pela posição do espaço em branco (0) no tabuleiro.
        """
        possible_moves = []
        blank_row, blank_col = self.blank_tile

        if blank_row > 0:
            possible_moves.append(Actions.UP)
        if blank_row < len(self.board) - 1:
            possible_moves.append(Actions.DOWN)
        if blank_col > 0:
            possible_moves.append(Actions.LEFT)
        if blank_col < len(self.board[0]) - 1:
            possible_moves.append(Actions.RIGHT)

        return possible_moves
    # get_possible_moves

    def get_path(self) -> List[State]:
        """
        Retorna o caminho percorrido para chegar ao estado atual.
        O caminho é representado como uma lista de estados.
        """
        path = [self]
        current_state = self

        while current_state.parent:
            path.append(current_state.parent)
            current_state = current_state.parent

        return path[::-1]  # Inverte a lista para mostrar o caminho do início ao fim
    # get_path

    def grid(self) -> List[List[int]]:
        """
        Retorna o tabuleiro do quebra-cabeça como uma lista de listas.
        """
        return self.board
# State
