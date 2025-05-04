from typing import List
from .state import State
from .algorithms import Algorithms, Heuristics
from search import bfs, dfs, astar, greedy, ucs

class Puzzle:
    """
    Classe principal que resolve o quebra-cabeça.
    Dados os estados inicial e objetivo, e o algoritmo a ser utilizado,
    resolve o quebra-cabeça e retorna a solução.
    """
    def __init__(self, initial_state: State, goal_state: State, 
                 algorithm: Algorithms = Algorithms.A_STAR, 
                 heuristic: Heuristics = Heuristics.MANHATTAN) -> None:
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.algorithm = algorithm
        self.heuristic = heuristic

        if not initial_state or not goal_state:
            raise ValueError("Initial and goal states cannot be empty.")
        if initial_state == goal_state:
            raise ValueError("Initial and goal states cannot be the same.")
        if not isinstance(initial_state, State) or not isinstance(goal_state, State):
            raise ValueError("Initial and goal states must be instances of State.")
        if not isinstance(algorithm, Algorithms):
            raise ValueError("Algorithms must be an instance of Algorithms.")
        if not isinstance(heuristic, Heuristics):
            raise ValueError("Heuristics must be an instance of Heuristics.")
        if algorithm in [Algorithms.A_STAR, Algorithms.GREEDY] and heuristic == Heuristics.NONE:
            raise ValueError("Heuristics must be specified for the selected algorithm.")
        if algorithm not in [Algorithms.A_STAR, Algorithms.GREEDY]:
            self.heuristic = Heuristics.NONE
    # __init__

    def solve(self) -> List[State]:
        """
        Resolve o quebra-cabeça usando o algoritmo especificado.
        Retorna a lista de estados que compõem a solução.
        """
        if self.algorithm == Algorithms.BFS:
            return bfs(self.initial_state, self.goal_state)
        elif self.algorithm == Algorithms.DFS:
            return dfs(self.initial_state, self.goal_state)
        elif self.algorithm == Algorithms.A_STAR:
            return astar(self.initial_state, self.goal_state, self.heuristic)
        elif self.algorithm == Algorithms.GREEDY:
            return greedy(self.initial_state, self.goal_state, self.heuristic)
        elif self.algorithm == Algorithms.UCS:
            return ucs(self.initial_state, self.goal_state)
        else:
            raise ValueError("Unknown algorithm specified.")
    # solve

    def reset(self) -> None:
        """
        Reinicia o quebra-cabeça para o estado inicial.
        """
        self.initial_state = State([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.goal_state = State([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    # reset
# Puzzle
