from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i: int = 0
        sums: list[list[int]] = []
        while i < len(nums) - 2:
            l: int = i + 1
            r: int = len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    s = [nums[i], nums[l], nums[r]]
                    if s not in sums:
                        sums.append(s)
                    l += 1
                    r -= 1
            i += 1

        return sums


def main() -> None:

    r1 = [[-1, -1, 2], [-1, 0, 1]] == Solution().threeSum(nums=[-1, 0, 1, 2, -1, -4])
    r2 = [] == Solution().threeSum(nums=[0, 1, 1])
    r3 = [[0, 0, 0]] == Solution().threeSum(nums=[0, 0, 0])
    r4 = [[0, 0, 0]] == Solution().threeSum(nums=[0, 0, 0, 0])
    r5 = [[-2, 0, 2], [-2, 1, 1]] == Solution().threeSum(nums=[-2, 0, 1, 1, 2])

    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)

    return None


if __name__ == "__main__":
    main()
