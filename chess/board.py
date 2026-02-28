from __future__ import annotations

from typing import Dict, Optional

from chess.pieces import Pawn, Rook, Bishop, BaseChessPiece


class Board:
    def __init__(self):
        # a1..h8
        self.squares: Dict[str, Optional[BaseChessPiece]] = {
            f"{chr(col)}{row}": None
            for col in range(ord("a"), ord("h") + 1)
            for row in range(1, 9)
        }

        self.setup_board()

        for square, piece in self.squares.items():
            if piece is not None:
                piece.set_initial_position(square)
                piece.define_board(self)

    def setup_board(self):
        # Black back rank
        self.squares["a1"] = Rook("BLACK", 1)
        self.squares["c1"] = Bishop("BLACK", 1)
        self.squares["f1"] = Bishop("BLACK", 2)
        self.squares["h1"] = Rook("BLACK", 2)

        # Black pawns row 2
        black_pawns = {f"{chr(col)}2": Pawn("BLACK", i + 1) for i, col in enumerate(range(ord("a"), ord("h") + 1))}
        self.squares.update(black_pawns)

        # White pawns row 7
        white_pawns = {f"{chr(col)}7": Pawn("WHITE", i + 1) for i, col in enumerate(range(ord("a"), ord("h") + 1))}
        self.squares.update(white_pawns)

        # White back rank
        self.squares["a8"] = Rook("WHITE", 1)
        self.squares["c8"] = Bishop("WHITE", 1)
        self.squares["f8"] = Bishop("WHITE", 2)
        self.squares["h8"] = Rook("WHITE", 2)

    def print_board(self):
        for row in range(1, 9):
            row_values = [self.squares[f"{chr(col)}{row}"] for col in range(ord("a"), ord("h") + 1)]
            print(row_values)

    def get_piece(self, square: str) -> Optional[BaseChessPiece]:
        """Returns the piece that is on a specific square"""
        return self.squares.get(square)

    def is_square_empty(self, square: str) -> bool:
        """Returns True if the square is empty, False otherwise."""
        return self.get_piece(square) is None

    def kill_piece(self, square: str):
        """Kill the piece on a square (if any)."""
        piece = self.get_piece(square)
        if piece is not None:
            piece.die()
            self.squares[square] = None

    def find_piece(self, symbol: str, identifier: int, color: str) -> Optional[BaseChessPiece]:
        matches = [
            piece
            for _, piece in self.squares.items()
            if piece is not None
            and piece.symbol == symbol
            and piece.identifier == identifier
            and piece.color == color
        ]
        return matches[0] if matches else None

    def move_piece(self, old_square: str, new_square: str) -> bool:
        if old_square not in self.squares or new_square not in self.squares:
            return False

        piece = self.squares[old_square]
        if piece is None:
            return False

        if self.squares[new_square] is not None:
            return False

        # move
        self.squares[old_square] = None
        self.squares[new_square] = piece
        piece.position = new_square
        return True