import heapq
from typing import List
from puzzle.state import State
from utils.util import build_path
from puzzle.algorithms import Heuristics
from heuristics.manhattan import h_manhattan
from heuristics.misplaced import h_misplaced

def greedy(initial_state: State, goal_state: State, 
           heuristic: Heuristics) -> List[State] | None:
    """
    Realiza a busca gulosa (Greedy Search) para encontrar o caminho do estado inicial ao estado objetivo.
    Retorna o caminho encontrado ou None se não houver solução.
    """
    heap = []

    # Escolhe a função heurística apropriada
    if heuristic == Heuristics.MANHATTAN:
        heuristic_fn = h_manhattan
    elif heuristic == Heuristics.MISPLACED:
        heuristic_fn = h_misplaced
    else:
        raise ValueError("Heuristics must be MANHATTAN or MISPLACED for Greedy Search")

    heapq.heappush(heap, (heuristic_fn(initial_state, goal_state), initial_state))

    visited = set()
    parents = {initial_state: None}

    while heap:
        _, current = heapq.heappop(heap)

        if current == goal_state:
            return build_path(current, parents)

        visited.add(hash(current))

        for action in current.get_possible_moves():
            neighbor = current.move(action)
            if neighbor is None:
                continue

            if hash(neighbor) not in visited:
                parents[neighbor] = current
                priority = heuristic_fn(neighbor, goal_state)
                heapq.heappush(heap, (priority, neighbor))
                visited.add(hash(neighbor))

    return None
# greedy
