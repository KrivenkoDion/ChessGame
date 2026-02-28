from chess.board import Board


if __name__ == "__main__":
    board = Board()
    board.setup_board()
    board.print_board()

    # Проверка поиска фигуры
    found = board.find_piece("-", 1, "WHITE")
    print("Found:", found)