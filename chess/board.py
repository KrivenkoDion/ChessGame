from __future__ import annotations

from typing import Dict, Optional, List

from chess.pieces import (
    Pawn, Rook, Knight, Bishop, Queen, King,
    BaseChessPiece,
)


class Board:
    def __init__(self):
        # keys: a1..h8, values: None or a chess piece
        self.squares: Dict[str, Optional[BaseChessPiece]] = {
            f"{chr(col)}{row}": None
            for col in range(ord("a"), ord("h") + 1)
            for row in range(1, 9)
        }

    def setup_board(self):
        # --- Black back rank (row 1) ---
        self.squares["a1"] = Rook("BLACK", 1)
        self.squares["b1"] = Knight("BLACK", 1)
        self.squares["c1"] = Bishop("BLACK", 1)
        self.squares["d1"] = Queen("BLACK", 1)
        self.squares["e1"] = King("BLACK", 1)
        self.squares["f1"] = Bishop("BLACK", 2)
        self.squares["g1"] = Knight("BLACK", 2)
        self.squares["h1"] = Rook("BLACK", 2)

        # --- White back rank (row 8) ---
        self.squares["a8"] = Rook("WHITE", 1)
        self.squares["b8"] = Knight("WHITE", 1)
        self.squares["c8"] = Bishop("WHITE", 1)
        self.squares["d8"] = Queen("WHITE", 1)
        self.squares["e8"] = King("WHITE", 1)
        self.squares["f8"] = Bishop("WHITE", 2)
        self.squares["g8"] = Knight("WHITE", 2)
        self.squares["h8"] = Rook("WHITE", 2)

        # --- Pawns via dict comprehension ---
        black_pawns = {f"{chr(col)}2": Pawn("BLACK", i)
                       for i, col in enumerate(range(ord("a"), ord("h") + 1), start=1)}
        white_pawns = {f"{chr(col)}7": Pawn("WHITE", i)
                       for i, col in enumerate(range(ord("a"), ord("h") + 1), start=1)}

        self.squares.update(black_pawns)
        self.squares.update(white_pawns)

    def print_board(self):
        # print row-first: 1..8
        for row in range(1, 9):
            row_values: List[Optional[BaseChessPiece]] = [
                self.squares[f"{chr(col)}{row}"]
                for col in range(ord("a"), ord("h") + 1)
            ]
            print(row_values)

    def find_piece(self, symbol: str, identifier: int, color: str) -> List[BaseChessPiece]:
        return [
            piece for _, piece in self.squares.items()
            if piece is not None
            and piece.symbol == symbol
            and piece.identifier == identifier
            and piece.color == color
        ]

    def get_piece(self, square: str) -> Optional[BaseChessPiece]:
        return self.squares[square]

    def is_square_empty(self, square: str) -> bool:
        return self.get_piece(square) is None

    def kill_piece(self, square: str):
        piece = self.get_piece(square)
        if piece is None:
            return
        piece.die()
        self.squares[square] = None