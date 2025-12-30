class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        single: int = 0
        for num in nums:
            single = single ^ num
        return single


def run_test(nums: list[int], expected: int) -> None:
    try:
        result = Solution().singleNumber(nums)
        ok = result == expected
        print(ok)
        if not ok:
            print(f"  nums:     {nums}")
            print(f"  expected: {expected}")
            print(f"  got:      {result}")
    except Exception as e:
        print(f"ERROR -> {e}")


def main() -> None:
    samples = [
        # Problem examples
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
        # Additional tests / edge cases
        ([0], 0),
        ([5, 5, 3], 3),
        ([-1, -1, -2], -2),
    ]

    for nums, expected in samples:
        run_test(nums, expected)


if __name__ == "__main__":
    main()
