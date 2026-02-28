from __future__ import annotations

import functools
from abc import ABC
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from chess.board import Board


def print_board(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        if self.board is not None:
            self.board.print_board()
        return result
    return wrapper


class BaseChessPiece(ABC):
    def __init__(self, color: str, name: str, symbol: str, identifier: int):
        self.color = color
        self.name = name
        self.symbol = symbol
        self.identifier = identifier
        self.position: str = "None"
        self.is_alive: bool = True
        self.board: Optional["Board"] = None

    def die(self):
        self.is_alive = False

    def set_initial_position(self, position: str):
        self.position = position

    def define_board(self, board: "Board"):
        self.board = board

    @print_board
    def move(self, movement: str):
        if self.board is None:
            return "No board attached"

        if movement not in self.board.squares:
            return f"Invalid square: {movement}"

        target = self.board.get_piece(movement)

        if target is not None:
            if target.color == self.color:
                return f"Blocked by own piece at {movement}"
            self.board.kill_piece(movement)

        old_pos = self.position
        self.board.squares[old_pos] = None
        self.position = movement
        self.board.squares[movement] = self

        return f"{self.name} moved from {old_pos} to {movement}"

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
        return super().move(new_pos)


class Rook(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Rook", "R", identifier)

    def move(self, direction: str, squares: int):
        if self.board is None:
            return "No board attached"
        from chess.board_movement import BoardMovement

        direction = direction.lower()
        if direction == "left":
            new_pos = BoardMovement.left(self.position, self.color, squares)
        elif direction == "right":
            new_pos = BoardMovement.right(self.position, self.color, squares)
        elif direction == "forward":
            new_pos = BoardMovement.forward(self.position, self.color, squares)
        elif direction == "backward":
            new_pos = BoardMovement.backward(self.position, self.color, squares)
        else:
            return "Invalid direction"

        return super().move(new_pos)


class Bishop(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Bishop", "B", identifier)

    def move(self):
        return "Bishop moves diagonally (stub)"