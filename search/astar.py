import heapq
from typing import List
from puzzle.state import State
from utils.util import build_path
from puzzle.algorithms import Heuristics
from heuristics.manhattan import h_manhattan
from heuristics.misplaced import h_misplaced

def astar(initial_state: State, goal_state: State, 
          heuristic: Heuristics) -> List[State] | None:
    """
    Realiza a busca A* para encontrar o caminho do estado inicial ao estado objetivo.
    Utiliza uma fila de prioridade para explorar os estados com menor custo total (g + h).
    Retorna o caminho encontrado ou None se não houver solução.
    """
    heap = []
    g_score = {initial_state: 0}

    # Escolhe a função heurística correta
    if heuristic == Heuristics.MANHATTAN:
        heuristic_fn = h_manhattan
    elif heuristic == Heuristics.MISPLACED:
        heuristic_fn = h_misplaced
    else:
        raise ValueError(f"Heuristics must be MANHATTAN or MISPLACED for A* = {heuristic}")

    f_score = {initial_state: heuristic_fn(initial_state, goal_state)}
    heapq.heappush(heap, (f_score[initial_state], initial_state))

    parents = {initial_state: None}
    visited = set()

    while heap:
        _, current = heapq.heappop(heap)

        if current == goal_state:
            return build_path(current, parents)

        visited.add(hash(current))

        for action in current.get_possible_moves():
            neighbor = current.move(action)
            if neighbor is None:
                continue

            tentative_g = g_score[current] + 1
            if neighbor in g_score and tentative_g >= g_score[neighbor]:
                continue

            if hash(neighbor) not in visited:
                parents[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic_fn(neighbor, goal_state)
                heapq.heappush(heap, (f_score[neighbor], neighbor))

    return None
# astar
