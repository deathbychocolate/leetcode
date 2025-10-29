from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for nums in matrix:
            l: int = 0
            r: int = len(nums) - 1
            mid: int = (l + r) // 2
            while l <= r:
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    print("An unexpected error occurred.")
                mid = (l + r) // 2
            print(f"Target {target} not found in row {nums}, moving to next row.")
        return False


def main() -> None:
    r1 = True == Solution().searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)
    r2 = False == Solution().searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)
    print(r1)
    print(r2)


if __name__ == "__main__":
    main()
