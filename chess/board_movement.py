class BoardMovement:
    @staticmethod
    def forward(position: str, color: str, squares: int = 1) -> str:
        col = position[0]
        row = int(position[1])

        if color == "WHITE":
            new_row = row - squares
        else:
            new_row = row + squares

        return f"{col}{new_row}"