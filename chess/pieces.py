from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from chess.board import Board


class BaseChessPiece(ABC):
    def __init__(self, color: str, name: str, symbol: str, identifier: int):
        self.color = color
        self.name = name
        self.symbol = symbol
        self.identifier = identifier
        self.position: str = "None"
        self.is_alive: bool = True
        self.board: Optional["Board"] = None

    @abstractmethod
    def move(self, *args, **kwargs):
        """Child classes must implement how they move."""
        raise NotImplementedError

    def die(self):
        self.is_alive = False

    def set_initial_position(self, position: str):
        self.position = position

    def define_board(self, board: "Board"):
        self.board = board

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"

    def __repr__(self):
        return self.__str__()


class Pawn(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Pawn", "-", identifier)

    def move(self):
        if self.board is None:
            return "No board attached"

        from chess.board_movement import BoardMovement

        new_pos = BoardMovement.forward(self.position, self.color, 1)
        moved = self.board.move_piece(self.position, new_pos)

        if moved:
            return f"Pawn moved from {self.position} to {new_pos}"
        return f"Pawn cannot move from {self.position} to {new_pos}"


class Rook(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Rook", "R", identifier)

    def move(self, direction: str, squares: int):
        return f"Rook moves {direction} by {squares} squares"


class Bishop(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Bishop", "B", identifier)

    def move(self):
        return "Bishop moves diagonally (stub)"