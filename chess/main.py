from chess.board import Board


if __name__ == "__main__":
    board = Board()
    board.print_board()

    # quick test for find_piece (как в твоём выводе Found: [WHITE Pawn 1])
    piece = board.find_piece("-", 1, "WHITE")
    print("Found:", piece)