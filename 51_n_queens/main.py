"""https://leetcode.com/problems/n-queens/"""

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        elif n == 2:
            return [[".", "."], [".", "."]]
        elif n == 3:
            return [[".", ".", "."], [".", ".", "."], [".", ".", "."]]

        board: list[list["str"]] = []

        return board


def main() -> None:
    result: list[list[str]] = [[]]
    for i in range(1,10):
        result = Solution().solveNQueens(n=i)
        print(f"Solution for n={i}:")
        print("=======================================")
        print(result)


if __name__ == "__main__":
    main()
