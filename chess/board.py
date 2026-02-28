from __future__ import annotations
from typing import Optional

from chess.pieces import (
    BaseChessPiece,
    Pawn, Rook, Knight, Bishop, Queen, King
)


class Board:
    def __init__(self):
        # create squares: a1..h8 -> None
        self.squares: dict[str, Optional[BaseChessPiece]] = {
            f"{chr(c)}{r}": None
            for c in range(ord("a"), ord("i"))   # a..h
            for r in range(1, 9)                 # 1..8
        }

        self.setup_board()

    def setup_board(self):
        # --- BLACK back rank on row 1 ---
        self.squares["a1"] = Rook("BLACK", 1)
        self.squares["b1"] = Knight("BLACK", 1)
        self.squares["c1"] = Bishop("BLACK", 1)
        self.squares["d1"] = Queen("BLACK", 1)
        self.squares["e1"] = King("BLACK", 1)
        self.squares["f1"] = Bishop("BLACK", 2)
        self.squares["g1"] = Knight("BLACK", 2)
        self.squares["h1"] = Rook("BLACK", 2)

        # --- BLACK pawns on row 2 ---
        black_pawns = {f"{chr(c)}2": Pawn("BLACK", i)
                       for i, c in enumerate(range(ord("a"), ord("i")), start=1)}
        self.squares.update(black_pawns)

        # --- WHITE pawns on row 7 ---
        white_pawns = {f"{chr(c)}7": Pawn("WHITE", i)
                       for i, c in enumerate(range(ord("a"), ord("i")), start=1)}
        self.squares.update(white_pawns)

        # --- WHITE back rank on row 8 ---
        self.squares["a8"] = Rook("WHITE", 1)
        self.squares["b8"] = Knight("WHITE", 1)
        self.squares["c8"] = Bishop("WHITE", 1)
        self.squares["d8"] = Queen("WHITE", 1)
        self.squares["e8"] = King("WHITE", 1)
        self.squares["f8"] = Bishop("WHITE", 2)
        self.squares["g8"] = Knight("WHITE", 2)
        self.squares["h8"] = Rook("WHITE", 2)

    def print_board(self):
        # print row-first: row 1..8 (как в примере)
        for r in range(1, 9):
            row_values = [self.squares[f"{chr(c)}{r}"] for c in range(ord("a"), ord("i"))]
            print(row_values)

    def find_piece(self, symbol: str, identifier: int, color: str) -> Optional[BaseChessPiece]:
        found = [
            piece
            for _, piece in self.squares.items()
            if piece is not None
            and piece.symbol == symbol
            and piece.identifier == identifier
            and piece.color == color
        ]
        return found[0] if found else None

    def get_piece(self, square: str) -> Optional[BaseChessPiece]:
        """Returns the piece that is on a specific square"""
        return self.squares[square]

    def is_square_empty(self, square: str) -> bool:
        """Returns True if the square is empty, False otherwise."""
        return self.get_piece(square) is None

    def kill_piece(self, square: str):
        piece = self.get_piece(square)
        if piece is not None:
            piece.die()
            self.squares[square] = None