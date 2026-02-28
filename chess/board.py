import json
from typing import Optional, Dict, Any

from chess.pieces import Pawn, Rook, Bishop, Knight, Queen, King, BaseChessPiece


class Board:
    def __init__(self):
        self.squares: Dict[str, Optional[BaseChessPiece]] = {
            f"{chr(c)}{r}": None
            for c in range(ord("a"), ord("i"))
            for r in range(1, 9)
        }
        self.setup_board()
        for square, piece in self.squares.items():
            if piece is not None:
                piece.set_initial_position(square)
                piece.define_board(self)

    def setup_board(self):
        self.squares["a1"] = Rook("BLACK", 1)
        self.squares["b1"] = Knight("BLACK", 1)
        self.squares["c1"] = Bishop("BLACK", 1)
        self.squares["d1"] = Queen("BLACK", 1)
        self.squares["e1"] = King("BLACK", 1)
        self.squares["f1"] = Bishop("BLACK", 2)
        self.squares["g1"] = Knight("BLACK", 2)
        self.squares["h1"] = Rook("BLACK", 2)

        black_pawns = {f"{chr(c)}2": Pawn("BLACK", i) for i, c in enumerate(range(ord("a"), ord("i")), start=1)}
        self.squares.update(black_pawns)

        white_pawns = {f"{chr(c)}7": Pawn("WHITE", i) for i, c in enumerate(range(ord("a"), ord("i")), start=1)}
        self.squares.update(white_pawns)

        self.squares["a8"] = Rook("WHITE", 1)
        self.squares["b8"] = Knight("WHITE", 1)
        self.squares["c8"] = Bishop("WHITE", 1)
        self.squares["d8"] = Queen("WHITE", 1)
        self.squares["e8"] = King("WHITE", 1)
        self.squares["f8"] = Bishop("WHITE", 2)
        self.squares["g8"] = Knight("WHITE", 2)
        self.squares["h8"] = Rook("WHITE", 2)

    def print_board(self):
        for row in range(1, 9):
            line = [self.squares[f"{chr(c)}{row}"] for c in range(ord("a"), ord("i"))]
            print(line)

    def get_piece(self, square: str) -> Optional[BaseChessPiece]:
        return self.squares.get(square)

    def is_square_empty(self, square: str) -> bool:
        return self.get_piece(square) is None

    def kill_piece(self, square: str) -> bool:
        piece = self.get_piece(square)
        if piece is None:
            return False
        piece.die()
        self.squares[square] = None
        return True

    def find_piece(self, symbol: str, identifier: int, color: str) -> Optional[BaseChessPiece]:
        found = [
            piece
            for _, piece in self.squares.items()
            if piece is not None and piece.symbol == symbol and piece.identifier == identifier and piece.color == color
        ]
        return found[0] if found else None

    def move_piece(self, old_square: str, new_square: str) -> bool:
        piece = self.get_piece(old_square)
        if piece is None:
            return False

        target = self.get_piece(new_square)
        if target is not None:
            if target.color == piece.color:
                return False
            target.die()

        self.squares[old_square] = None
        self.squares[new_square] = piece
        piece.position = new_square
        return True

    def save_board(self, filename: str = "board.txt"):
        state: Dict[str, Any] = {}
        for square, piece in self.squares.items():
            state[square] = None if piece is None else piece.to_dict()

        with open(filename, "a", encoding="utf-8") as f:
            f.write(json.dumps(state, ensure_ascii=False) + "\n")