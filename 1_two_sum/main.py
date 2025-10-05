from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict: dict[int, int] = {num: index for index, num in enumerate(nums)}
        complement: int | None = None
        for index, num in enumerate(nums):
            complement = target - num
            if nums_dict.get(complement) and index != nums_dict[complement]:
                return [index, nums_dict[complement]]
        return []
        # # O(n^2) algorithm
        # for index1, num1 in enumerate(nums):
        #     for index2, num2 in enumerate(nums):
        #         if index1 != index2 and target == num1 + num2:
        #             return [index1, index2]
        # return []


def main() -> None:
    r1 = [0, 1] == Solution().twoSum(nums = [2,7,11,15], target = 9)
    r2 = [1, 2] == Solution().twoSum(nums = [3,2,4], target = 6)
    r3 = [0, 1] == Solution().twoSum(nums = [3,3], target = 6)
    print(r1)
    print(r2)
    print(r3)


if __name__=="__main__":
    main()