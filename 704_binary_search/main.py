from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l: int = 0
        r: int = len(nums) - 1
        mid: int = (l + r) // 2
        while l <= r:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                print("An unexpected exception occurred.")
            mid = (l + r) // 2
        return -1


def main() -> None:
    r1 = 4 == Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=9)
    r2 = -1 == Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=2)
    print(r1)
    print(r2)


if __name__ == "__main__":
    main()
