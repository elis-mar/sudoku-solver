def is_legal_move(board: list[list[int]], row: int, column: int, inserted_value: int) -> bool:
    # check row
    if inserted_value in board[row]:
        return False

    # check column
    for r in range(len(board)):
        if inserted_value == board[r][column]:
            return False

    # check box
    box_row, box_column = (row // 3) * 3, (column // 3) * 3
    for r in range(3):
        for c in range(3):
            if board[box_row + r][box_column + c] == inserted_value:
                return False

    return True

def find_next_emtpy_cell(board: list[list[int]]) -> tuple[int, int]:
    n = len(board)

    for row in range(n):
        for column in range(n):
            if board[row][column] == 0:
                return (row, column)

    return (-1, -1) # no empty cells

def solve(board: list[list[int]], numbers: list[int]) -> bool:
    empty_cell = find_next_emtpy_cell(board)
    if empty_cell == (-1, -1):
        return True

    (row, column) = empty_cell

    for number in numbers:
        if is_legal_move(board, row, column, number):
            board[row][column] = number

            if solve(board, numbers):
                return True

        board[row][column] = 0

    return False
