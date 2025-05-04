from puzzle.state import State

def h_manhattan(state: State, goal: State) -> int:
    """
    Heurística de distância de Manhattan.
    Calcula a soma das distâncias de Manhattan de cada peça em relação à sua posição no estado objetivo.
    """
    total = 0
    positions = {}
    for i in range(len(goal.board)):
        for j in range(len(goal.board[0])):
            positions[goal.board[i][j]] = (i, j)

    for i in range(len(state.board)):
        for j in range(len(state.board[0])):
            value = state.board[i][j]
            if value != 0:
                goal_i, goal_j = positions[value]
                total += abs(i - goal_i) + abs(j - goal_j)
    return total
# h_manhattan
