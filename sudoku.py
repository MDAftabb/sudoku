import copy
import random


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

def make_full_board():
    board = [[0] * 9 for _ in range(9)]

    def fill(b):
        cell = find_empty(b)
        if cell is None:
            return True

        row, col = cell
        numbers = list(range(1, 10))
        random.shuffle(numbers)
        for num in numbers:
            if is_valid(b, row, col, num):
                b[row][col] = num
                if fill(b):
                    return True
                b[row][col] = 0
        return False

    fill(board)
    return board

def count_solutions(board, limit=2):
    cell = find_empty(board)
    if cell is None:
        return 1  # the board is full: that is one complete solution
 
    row, col = cell
    total = 0
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            total += count_solutions(board, limit - total)
            board[row][col] = 0
            if total >= limit:
                break
    return total

def make_puzzle(solution, clues):
    puzzle = copy.deepcopy(solution) 
 
    cells = [(row, col) for row in range(9) for col in range(9)]
    random.shuffle(cells)
 
    filled = 81
    for row, col in cells:
        if filled <= clues:
            break
        saved = puzzle[row][col]
        puzzle[row][col] = 0
        if count_solutions(copy.deepcopy(puzzle)) != 1:
            puzzle[row][col] = saved 
        else:
            filled -= 1
    return puzzle
 
 
def board_to_string(board):
    return "".join(str(value) for row in board for value in row)

def run_tests():
    
    assert is_valid(PUZZLE, 0, 3, 3) is False
    assert is_valid(PUZZLE,0 ,3 ,8) is False
    assert is_valid(PUZZLE, 0, 3, 9) is False
    assert is_valid(PUZZLE, 0, 3, 2) is True
    assert is_valid(PUZZLE,0, 2, 4) is True
    print("All tests passed")


if __name__ =="__main__":
    run_tests()
     
    full = make_full_board()
    print_board(full)
    print(find_empty(full))                              
 
    # count_solutions
    print(count_solutions(copy.deepcopy(PUZZLE)))       
    print(count_solutions([[0] * 9 for _ in range(9)]))  
 
    # make_puzzle
    puzzle = make_puzzle(full, 30)
    print_board(puzzle)
    print(count_solutions(copy.deepcopy(puzzle)))        
 
    # board_to_string
    print(board_to_string(PUZZLE))


    