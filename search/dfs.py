from typing import List
from puzzle.state import State
from utils.util import build_path

def dfs(initial_state: State, goal_state: State, 
        depth_limit: int = 50) -> List[State] | None:
    """
    Realiza a busca em profundidade (DFS) para encontrar o caminho do estado inicial ao estado objetivo.
    Limita a profundidade da busca para evitar loops infinitos.
    Retorna o caminho encontrado ou None se não houver solução.
    """
    stack = [(initial_state, 0)]
    visited = set()
    parents = {initial_state: None}

    while stack:
        current, depth = stack.pop()
        if current == goal_state:
            return build_path(current, parents)

        if depth >= depth_limit:
            continue

        if hash(current) not in visited:
            visited.add(hash(current))

        for action in current.get_possible_moves():
                neighbor = current.move(action)
                
                if neighbor and hash(neighbor) not in visited:
                    parents[neighbor] = current
                    stack.append((neighbor, depth + 1))
    return None
# dfs
