import json
import random

from sudoku import make_full_board, make_puzzle, board_to_string

DIFFICULTIES = {
    "easy":   (36, 40),
    "medium": (31, 35),
    "hard":   (27, 30),
    "expert": (24, 26),
}
PUZZLES_PER_LEVEL = 15

def main():
    all_puzzles = {}

    for name, (low, high) in DIFFICULTIES.items():
        all_puzzles[name] = []
        for number in range(1, PUZZLES_PER_LEVEL + 1):
            clues = random.randint(low, high)
            solution = make_full_board()
            puzzle = make_puzzle(solution, clues)

            all_puzzles[name].append({
                "number": number,
                "puzzle": board_to_string(puzzle),
                "solution": board_to_string(solution),
            })
            print(f"{name} {number}/{PUZZLES_PER_LEVEL} done")

    with open("puzzles.json", "w") as f:
        json.dump(all_puzzles, f, indent=2)
    print("Saved puzzles.json")


if __name__ == "__main__":
    main()