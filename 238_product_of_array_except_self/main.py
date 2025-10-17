from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len: int = len(nums)
        products: list[int] = [1] * nums_len
        left_product = 1
        right_product = 1
        for i in range(nums_len):  # left product
            products[i] = left_product
            left_product *= nums[i]
        for j in range(nums_len - 1, -1, -1):  # right product
            products[j] *= right_product
            right_product *= nums[j]
        return products


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         products: list[int] = []
#         n: int = 0
#         while n < len(nums):
#             products.append(self.product(nums.copy(), n))
#             n += 1
#         return products

#     def product(self, nums: list[int], index: int) -> int:
#         del nums[index]
#         product: int = 1
#         for item in nums:
#             product *= item
#         return product


def main() -> None:
    r1: bool = [24, 12, 8, 6] == Solution().productExceptSelf([1, 2, 3, 4])
    r2: bool = [0, 0, 9, 0, 0] == Solution().productExceptSelf([-1, 1, 0, -3, 3])
    r3: bool = [0, 0] == Solution().productExceptSelf([0, 0])
    print(r1)
    print(r2)
    print(r3)


if __name__ == "__main__":
    main()
