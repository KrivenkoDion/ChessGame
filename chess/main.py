from chess.pieces import Pawn, Rook, Bishop

if __name__ == "__main__":

    pawn1 = Pawn("WHITE", 1)
    rook1 = Rook("BLACK", 1)
    bishop1 = Bishop("WHITE", 2)

    print(pawn1)
    print(rook1)
    print(bishop1)

    print(pawn1.move())
    print(rook1.move())
    print(bishop1.move())