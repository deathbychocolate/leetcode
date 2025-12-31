class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        missing: int = 0
        expected: int = 0
        actual: int = 0
        for num in range(len(nums) + 1):
            expected ^= num
        for num in nums:
            actual ^= num

        missing = expected ^ actual

        return missing


def run_test(nums: list[int], expected: int) -> None:
    try:
        result = Solution().missingNumber(nums)
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
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        # Additional tests / edge cases
        ([0], 1),
        ([1], 0),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0),
        ([0, 2], 1),
    ]

    for nums, expected in samples:
        run_test(nums, expected)


if __name__ == "__main__":
    main()
