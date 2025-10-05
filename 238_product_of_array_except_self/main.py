from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product: int | None = None
        l: list[int] = []
        for index, num in enumerate(nums):
            for num in nums:
                if nums[index] == num:
                    continue
                if product is None:
                    product = num
                else:
                    product *= num
            l.append(product)
            product = None
        return l


def main() -> None:
    # r1: bool = [24,12,8,6] == Solution().productExceptSelf([1,2,3,4])
    # r2: bool = [0,0,9,0,0] == Solution().productExceptSelf([-1,1,0,-3,3])
    r3: bool = [0,0] == Solution().productExceptSelf([0,0])
    # print(r1)
    # print(r2)
    print(r3)

if __name__ == "__main__":
    main()
