from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row_count: int = len(matrix)
        row_length_total: int = 0
        for nums in matrix:
            row_length_total += len(nums)
        row_length: int = row_length_total // row_count

        # [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

        l: int = 0
        r: int = row_length_total - 1
        mid: int = (l + r) // 2
        row: int = 0
        while l <= r:

            # determine which row to look at.
            if row_count > 1:
                row = mid // row_length
                mid -= row_length * row

            # found, right, or left?
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                mid += row_length * row
                l = mid + 1
            elif matrix[row][mid] > target:
                mid += row_length * row
                r = mid - 1
            else:
                print("An unexpected error occurred.")

            mid = (l + r) // 2

        return False


def main() -> None:
    r1 = True == Solution().searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3)
    r2 = False == Solution().searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13)
    r3 = False == Solution().searchMatrix(matrix=[[1]], target=0)
    r4 = False == Solution().searchMatrix(matrix=[[1], [3]], target=0)
    print(r1)
    print(r2)
    print(r3)
    print(r4)


if __name__ == "__main__":
    main()
