from enum import Enum, auto

class Algorithms(Enum):
    """
    Classe representando os algoritmos de busca disponíveis para resolver o quebra-cabeça.
    Os algoritmos disponíveis são:
    - BFS: Busca em Largura
    - DFS: Busca em Profundidade
    - A_STAR: Algoritmo A* (A estrela)
    - GREEDY: Algoritmo Guloso (Greedy)
    - UCS: Busca Uniforme (Uniform Cost Search)
    """
    BFS = auto()
    DFS = auto()
    A_STAR = auto()
    GREEDY = auto()
    UCS = auto()
# Algorithm

class Heuristics(Enum):
    """
    Classe representando as heurísticas disponíveis para os algoritmos.
    As heurísticas disponíveis são:
    - MANHATTAN: Distância de Manhattan
    - MISPLACED: Número de peças fora do lugar
    """
    NONE = auto()
    MANHATTAN = auto()
    MISPLACED = auto()
# Heuristic
