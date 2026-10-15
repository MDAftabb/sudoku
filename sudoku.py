import copy


PUZZLE = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


def print_board(board):
    for row_index, row in enumerate(board):
        if row_index in ((3,6)):
            print("------+-------+------")

        pieces=[]
        for col_index, value in enumerate(row):
            if col_index in (3,6):
                pieces.append("|")
            pieces.append(str(value)if value != 0 else ".")

        print(" ".join(pieces))

def is_valid(board,row,col,num):
    if num in board[row]:
        return False
    for r in range(9):
        if board[r][col]== num:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False
    return True

def find_empty(board):
    for r in range(9):
            for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None

def solve(board):
    cell= find_empty(board)
    if cell is None:
        return True

    row, col = cell
    for num in range(1,10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0

    return False

def run_tests():
    
    assert is_valid(PUZZLE, 0, 3, 3) is False
    assert is_valid(PUZZLE,0 ,3 ,8) is False
    assert is_valid(PUZZLE, 0, 3, 9) is False
    assert is_valid(PUZZLE, 0, 3, 2) is True
    assert is_valid(PUZZLE,0, 2, 4) is True
    print("All tests passed")


if __name__ =="__main__":
    print_board(PUZZLE)
    run_tests()

    board = copy.deepcopy(PUZZLE)
    print(solve(board))
    print_board(board)
    print(PUZZLE[0][2]) No newline at end of file
    
