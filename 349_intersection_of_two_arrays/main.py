from collections import defaultdict

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Optimal but shorter.
        return list(set(nums1) & set(nums2))

        # # Optimal using hash set subtraction.
        # return list(set(nums1) - (set(nums1) - set(nums2)))

        ## Naive and slow solution (improved further): Counting numbers after converting to sets.
        # count: dict[int, int] = defaultdict(int)
        # for num in set(nums1):
        #     count[num] += 1
        # for num in set(nums2):
        #     count[num] += 1

        # return [key for key, value in count.items() if value > 1]

        # # Naive and slow solution (improved): Counting numbers after converting to sets.
        # count: dict[int, int] = defaultdict(int)
        # for num in set(nums1):
        #     count[num] += 1
        # for num in set(nums2):
        #     count[num] += 1

        # intersection = []
        # for key, value in count.items():
        #     if value > 1:
        #         intersection.append(key)

        # return intersection

        # # Naive and slow solution: Counting numbers after converting to sets.
        # nums1 = set(nums1)
        # nums2 = set(nums2)
        # count = defaultdict(int)
        # for num in nums1:
        #     count[num] += 1
        # for num in nums2:
        #     count[num] += 1

        # intersection = []
        # for key, value in count.items():
        #     if value > 1:
        #         intersection.append(key)

        # return intersection



def run_test(nums1, nums2, expected):
    try:
        result = Solution().intersection(nums1, nums2)
        # Since order doesn't matter, compare as sets
        ok = set(result) == set(expected)
        print(ok)
        if not ok:
            print(f"  nums1:    {nums1}")
            print(f"  nums2:    {nums2}")
            print(f"  expected: {expected}")
            print(f"  got:      {result}")
    except Exception as e:
        print(f"ERROR -> {e}")


def main() -> None:
    samples = [
        # Problem examples
        ([1, 2, 2, 1], [2, 2], [2]),
        ([4, 9, 5], [9, 4, 9, 8, 4], [9, 4]),
        # Additional tests / edge cases
        ([1, 2, 3], [4, 5, 6], []),
        ([1], [1], [1]),
    ]

    for nums1, nums2, expected in samples:
        run_test(nums1, nums2, expected)


if __name__ == "__main__":
    main()
