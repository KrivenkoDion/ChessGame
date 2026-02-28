from __future__ import annotations

import functools
from abc import ABC, abstractmethod
from typing import Optional, TYPE_CHECKING

from chess.board_movement import BoardMovement

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

    def die(self):
        self.is_alive = False

    def set_initial_position(self, position: str):
        self.position = position

    def define_board(self, board: "Board"):
        self.board = board

    def to_dict(self):
        return {
            "color": self.color,
            "name": self.name,
            "symbol": self.symbol,
            "identifier": self.identifier,
            "position": self.position,
            "is_alive": self.is_alive,
        }

    @staticmethod
    def _print_board(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            if self.board is not None:
                self.board.print_board()
            return result
        return wrapper

    @staticmethod
    def _save_board(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            if self.board is not None:
                self.board.save_board()
            return result
        return wrapper

    @abstractmethod
    def move(self, *args, **kwargs):
        raise NotImplementedError

    @_save_board
    @_print_board
    def base_move(self, movement: str) -> bool:
        if self.board is None:
            return False
        return self.board.move_piece(self.position, movement)

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"

    def __repr__(self):
        return self.__str__()


class Pawn(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Pawn", "-", identifier)

    def move(self):
        new_pos = BoardMovement.forward(self.position, self.color, 1)
        ok = self.base_move(new_pos)
        return ok


class Rook(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Rook", "R", identifier)

    def move(self, direction: str, squares: int):
        if direction == "Left":
            new_pos = BoardMovement.left(self.position, self.color, squares)
        elif direction == "Right":
            new_pos = BoardMovement.right(self.position, self.color, squares)
        elif direction == "Forward":
            new_pos = BoardMovement.forward(self.position, self.color, squares)
        elif direction == "Backward":
            new_pos = BoardMovement.backward(self.position, self.color, squares)
        else:
            return False
        return self.base_move(new_pos)


class Bishop(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Bishop", "B", identifier)

    def move(self, direction: str, squares: int):
        if direction == "ForwardLeft":
            new_pos = BoardMovement.forward_left(self.position, self.color, squares)
        elif direction == "ForwardRight":
            new_pos = BoardMovement.forward_right(self.position, self.color, squares)
        elif direction == "BackwardLeft":
            new_pos = BoardMovement.backward_left(self.position, self.color, squares)
        elif direction == "BackwardRight":
            new_pos = BoardMovement.backward_right(self.position, self.color, squares)
        else:
            return False
        return self.base_move(new_pos)


class Knight(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Knight", "N", identifier)

    def move(self, direction: str):
        if direction == "ForwardLeft":
            new_pos = BoardMovement.knight_forward_left(self.position, self.color)
        elif direction == "ForwardRight":
            new_pos = BoardMovement.knight_forward_right(self.position, self.color)
        elif direction == "LeftForward":
            new_pos = BoardMovement.knight_left_forward(self.position, self.color)
        elif direction == "RightForward":
            new_pos = BoardMovement.knight_right_forward(self.position, self.color)
        elif direction == "BackwardLeft":
            new_pos = BoardMovement.knight_backward_left(self.position, self.color)
        elif direction == "BackwardRight":
            new_pos = BoardMovement.knight_backward_right(self.position, self.color)
        elif direction == "LeftBackward":
            new_pos = BoardMovement.knight_left_backward(self.position, self.color)
        elif direction == "RightBackward":
            new_pos = BoardMovement.knight_right_backward(self.position, self.color)
        else:
            return False
        return self.base_move(new_pos)


class Queen(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Queen", "Q", identifier)

    def move(self, direction: str, squares: int):
        mapping = {
            "Left": BoardMovement.left,
            "Right": BoardMovement.right,
            "Forward": BoardMovement.forward,
            "Backward": BoardMovement.backward,
            "ForwardLeft": BoardMovement.forward_left,
            "ForwardRight": BoardMovement.forward_right,
            "BackwardLeft": BoardMovement.backward_left,
            "BackwardRight": BoardMovement.backward_right,
        }
        if direction not in mapping:
            return False
        new_pos = mapping[direction](self.position, self.color, squares)
        return self.base_move(new_pos)


class King(BaseChessPiece):
    def __init__(self, color: str, identifier: int):
        super().__init__(color, "King", "K", identifier)

    def move(self, direction: str):
        mapping = {
            "Left": lambda p, c: BoardMovement.left(p, c, 1),
            "Right": lambda p, c: BoardMovement.right(p, c, 1),
            "Forward": lambda p, c: BoardMovement.forward(p, c, 1),
            "Backward": lambda p, c: BoardMovement.backward(p, c, 1),
            "ForwardLeft": lambda p, c: BoardMovement.forward_left(p, c, 1),
            "ForwardRight": lambda p, c: BoardMovement.forward_right(p, c, 1),
            "BackwardLeft": lambda p, c: BoardMovement.backward_left(p, c, 1),
            "BackwardRight": lambda p, c: BoardMovement.backward_right(p, c, 1),
        }
        if direction not in mapping:
            return False
        new_pos = mapping[direction](self.position, self.color)
        return self.base_move(new_pos)