# chess/board.py
from __future__ import annotations

from typing import Optional

from chess.pieces import Pawn, Rook, Bishop, BaseChessPiece


class Board:
    def __init__(self):
        self.squares = {f"{chr(c)}{r}": None for c in range(ord("a"), ord("i")) for r in range(1, 9)}
        self.setup_board()
        for square, piece in self.squares.items():
            if piece is not None:
                piece.set_initial_position(square)
                piece.define_board(self)

    def setup_board(self):
        self.squares["a1"] = Rook("BLACK", 1)
        self.squares["b1"] = None
        self.squares["c1"] = Bishop("BLACK", 1)
        self.squares["d1"] = None
        self.squares["e1"] = None
        self.squares["f1"] = Bishop("BLACK", 2)
        self.squares["g1"] = None
        self.squares["h1"] = Rook("BLACK", 2)

        self.squares.update({f"{chr(c)}2": Pawn("BLACK", idx) for idx, c in enumerate(range(ord("a"), ord("i")), start=1)})
        self.squares.update({f"{chr(c)}7": Pawn("WHITE", idx) for idx, c in enumerate(range(ord("a"), ord("i")), start=1)})

        self.squares["a8"] = Rook("WHITE", 1)
        self.squares["b8"] = None
        self.squares["c8"] = Bishop("WHITE", 1)
        self.squares["d8"] = None
        self.squares["e8"] = None
        self.squares["f8"] = Bishop("WHITE", 2)
        self.squares["g8"] = None
        self.squares["h8"] = Rook("WHITE", 2)

    def print_board(self):
        for row in range(8, 0, -1):
            line = [self.squares[f"{col}{row}"] for col in "abcdefgh"]
            print(line)

    def find_piece(self, symbol: str, identifier: int, color: str) -> Optional[BaseChessPiece]:
        matches = [
            piece
            for _, piece in self.squares.items()
            if piece is not None and piece.symbol == symbol and piece.identifier == identifier and piece.color == color
        ]
        return matches[0] if matches else None

    def get_piece(self, square: str):
        return self.squares[square]

    def is_square_empty(self, square: str) -> bool:
        return self.get_piece(square) is None

    def kill_piece(self, square: str) -> None:
        piece = self.get_piece(square)
        if piece is not None:
            piece.die()
            self.squares[square] = None

    def move_piece(self, old_square: str, new_square: str) -> bool:
        if old_square not in self.squares or new_square not in self.squares:
            return False
        piece = self.squares[old_square]
        if piece is None:
            return False
        if self.squares[new_square] is not None:
            return False
        self.squares[old_square] = None
        self.squares[new_square] = piece
        piece.position = new_square
        return True