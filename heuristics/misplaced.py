from puzzle.state import State

def h_misplaced(state: State, goal: State) -> int:
    """
    Heurística de peças fora do lugar.
    Conta o número de peças que estão fora do lugar em relação ao estado objetivo.
    """
    count = 0
    for i in range(len(state.board)):
        for j in range(len(state.board[0])):
            if state.board[i][j] != 0 and state.board[i][j] != goal.board[i][j]:
                count += 1
    return count
# # h_misplaced
