from enum import Enum, auto

class Actions(Enum):
    """
    Classe representando as ações possíveis no quebra-cabeça.
    As ações são representadas por direções: cima, baixo, esquerda e direita.
    O valor 0 representa uma ação automática, que não faz nada.
    """
    NO_OP = auto()  # No action
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
# Action
