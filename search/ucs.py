import heapq
from typing import List
from itertools import count
from puzzle.state import State
from utils.util import build_path

def ucs(initial_state: State, goal_state: State) -> List[State] | None:
    """
    Realiza a busca de custo uniforme (UCS) para encontrar o caminho do estado inicial ao estado objetivo.
    Utiliza uma fila de prioridade para explorar os estados com menor custo.
    Retorna o caminho encontrado ou None se não houver solução.
    """
    heap = []
    counter = count()  # contador incremental para desempatar
    cost = {initial_state: 0}
    heapq.heappush(heap, (0, next(counter), initial_state))

    parents = {initial_state: None}
    visited = set()

    while heap:
        _, _, current = heapq.heappop(heap)

        if current == goal_state:
            return build_path(current, parents)

        visited.add(hash(current))

        for action in current.get_possible_moves():
            neighbor = current.move(action)
            if neighbor is None:
                continue

            new_cost = cost[current] + 1
            if neighbor in cost and new_cost >= cost[neighbor]:
                continue

            if hash(neighbor) not in visited:
                cost[neighbor] = new_cost
                parents[neighbor] = current
                heapq.heappush(heap, (new_cost, next(counter), neighbor))
    return None
# csu
