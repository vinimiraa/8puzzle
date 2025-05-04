# utils/util.py

from typing import List
from puzzle.state import State

def build_path(state: State, parents: dict) -> List:
    """
    Constrói o caminho percorrido a partir do estado inicial até o estado atual.
    O caminho é representado como uma lista de estados.
    """
    path = []
    while state:
        path.append(state)
        state = parents.get(state)
    return list(reversed(path))
# build_path
