from typing import Any, List
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # checks rows
        count: defaultdict[Any, int] = defaultdict(int)
        for row in board:
            for num in row:
                if num != ".":
                    count[num] += 1
                if count[num] > 1:
                    return False
            count = defaultdict(int)

        # check columns
        count = defaultdict(int)
        for i in range(9):
            for j in range(9):
                for num in board[j][i]:
                    if num != ".":
                        count[num] += 1
                    if count[num] > 1:
                        return False
            count = defaultdict(int)

        # check boxes
        count = defaultdict(int)
        for box in range(9):
            for i in range(3):
                for j in range(3):
                    row_index = (box // 3) * 3 + i
                    col_index = (box % 3) * 3 + j
                    for num in board[row_index][col_index]:
                        if num != ".":
                            count[num] += 1
                        if count[num] > 1:
                            return False
            count = defaultdict(int)

        return True


def main() -> None:
    board_1: list[list[str]] = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    board_2: list[list[str]] = [  # two 8s in 1st column
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    board_3: list[list[str]] = [
        ["7", ".", ".", ".", "4", ".", ".", ".", "."],
        [".", ".", ".", "8", "6", "5", ".", ".", "."],
        [".", "1", ".", "2", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "9", ".", ".", "."],
        [".", ".", ".", ".", "5", ".", "5", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]
    board_4: list[list[str]] = [
        [".", ".", ".", ".", "5", ".", ".", "1", "."],
        [".", "4", ".", "3", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "3", ".", ".", "1"],
        ["8", ".", ".", ".", ".", ".", ".", "2", "."],
        [".", ".", "2", ".", "7", ".", ".", ".", "."],
        [".", "1", "5", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "2", ".", ".", "."],
        [".", "2", ".", "9", ".", ".", ".", ".", "."],
        [".", ".", "4", ".", ".", ".", ".", ".", "."],
    ]
    r1 = True == Solution().isValidSudoku(board=board_1)
    r2 = False == Solution().isValidSudoku(board=board_2)
    r3 = False == Solution().isValidSudoku(board=board_3)
    r4 = False == Solution().isValidSudoku(board=board_4)
    print(r1)
    print(r2)
    print(r3)
    print(r4)


if __name__ == "__main__":
    main()
