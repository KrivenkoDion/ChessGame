from chess.pieces import Pawn, Rook, Bishop, Queen, King, Knight


if __name__ == "__main__":

    pieces = [
        Pawn("WHITE", 1),
        Rook("BLACK", 1),
        Bishop("WHITE", 2),
        Queen("BLACK", 1),
        King("WHITE", 1),
        Knight("BLACK", 2)
    ]

    for piece in pieces:
        print(piece)
        print(piece.move())
        print("-" * 30)