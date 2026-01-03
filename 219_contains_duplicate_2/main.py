# from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        # Optimal solution | Single Pass | O(n) | 19 ms - 28 ms | Greatly reduced memory allocation
        d: dict[int, int] = {}
        for index, num in enumerate(nums):
            if num in d and index - d[num] <= k:
                return True
            d[num] = index

        return False

        # # Improved solution | Single Pass | O(n) | 75 ms - 87 ms
        # d: defaultdict = defaultdict(list)
        # for index, num in enumerate(nums):
        #     d[num].append(index)
        #     if len(d[num]) > 1 and abs(d[num][-1] - d[num][-2]) <= k:
        #         return True

        # return False

        # # Naive - Brute Force solution - O(n*Min(n,k))
        # i: int = 0
        # j: int = 1
        # while i < len(nums) - 1:
        #     j = i + 1
        #     while j < len(nums):
        #         if abs(i - j) > k:
        #             break
        #         if i != j and nums[i] == nums[j]:
        #             return True
        #         j += 1
        #     i += 1

        # return False


def run_test(nums, k, expected):
    try:
        result = Solution().containsNearbyDuplicate(nums, k)
        ok = result == expected
        print(ok)
        if not ok:
            print(f"  input:    nums={nums}, k={k}")
            print(f"  expected: {expected}")
            print(f"  got:      {result}")
    except Exception as e:
        print(f"ERROR -> {e}")


def main() -> None:
    samples = [
        # Problem examples
        ([1, 2, 3, 1], 3, True),
        ([1, 0, 1, 1], 1, True),
        ([1, 2, 3, 1, 2, 3], 2, False),
        # Additional tests / edge cases
        ([1, 2, 3, 4, 5], 3, False),
        ([1], 1, False),
        ([1, 1], 1, True),
    ]

    for nums, k, expected in samples:
        run_test(nums, k, expected)


if __name__ == "__main__":
    main()
