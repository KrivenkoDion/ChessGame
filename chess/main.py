from chess.board import Board

if __name__ == "__main__":
    board = Board()
    board.print_board()

    pawn = board.find_piece("-", 1, "WHITE")
    print("Found:", pawn)

    if pawn:
        pawn.move()