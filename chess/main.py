# chess/main.py
from chess.board import Board


if __name__ == "__main__":
    board = Board()
    board.print_board()

    pawn = board.find_piece("-", 1, "WHITE")
    print("Found:", pawn)

    if pawn:
        print(pawn.move())
        board.print_board()

    print("a6 empty?", board.is_square_empty("a6"))
    board.kill_piece("a6")
    print("a6 empty after kill?", board.is_square_empty("a6"))
    board.print_board()