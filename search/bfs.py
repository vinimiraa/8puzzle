from typing import List
from collections import deque
from puzzle.state import State
from utils.util import build_path

def bfs(initial_state: State, goal_state: State) -> List[State] | None:
    """
    Realiza a busca em largura (BFS) para encontrar o caminho do estado inicial ao estado objetivo.
    Utiliza uma fila para explorar os estados em ordem de profundidade.
    Retorna o caminho encontrado ou None se não houver solução.
    """
    queue = deque([initial_state])
    visited = set()
    visited.add(hash(initial_state))

    parents = {initial_state: None}

    while queue:
        current = queue.popleft()

        if current == goal_state:
            return build_path(current, parents)

        for action in current.get_possible_moves():
            neighbor = current.move(action)
            if neighbor and hash(neighbor) not in visited:
                visited.add(hash(neighbor))
                parents[neighbor] = current
                queue.append(neighbor)

    return None
# bfs
