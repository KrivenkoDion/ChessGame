from __future__ import annotations
from abc import ABC, abstractmethod

class BaseChessPiece(ABC):
    def __init__(self, color: str, name: str, symbol: str, identifier: int):
        self.color = color            # "BLACK" or "WHITE"
        self.name = name              # "Pawn", "Rook", ...
        self.symbol = symbol          # '-', 'R', 'B', 'N', 'K', 'Q'
        self.identifier = identifier  # 1..8 (or 1..2 for some)
        self.position = "None"
        self.is_alive = True

    @abstractmethod
    def move(self):
        """For now: return a string. Later: real movement."""
        pass

    def die(self):
        self.is_alive = False

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"

    def __repr__(self):
        return self.__str__()


class Pawn(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Pawn", "-", identifier)

    def move(self):
        return "Pawn moves forward 1 position"


class Rook(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Rook", "R", identifier)

    def move(self):
        return "Rook moves in a straight line"


class Bishop(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Bishop", "B", identifier)

    def move(self):
        return "Bishop moves diagonally"


class Knight(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Knight", "N", identifier)

    def move(self):
        return "Knight moves in an L shape"


class King(BaseChessPiece):
    def __init__(self, color: str, identifier: int = 1):
        super().__init__(color, "King", "K", identifier)

    def move(self):
        return "King moves 1 square in any direction"


class Queen(BaseChessPiece):
    def __init__(self, color: str, identifier: int = 1):
        super().__init__(color, "Queen", "Q", identifier)

    def move(self):
        return "Queen moves like rook and bishop"