class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        subsets: list[list[int]] = []
        for i in range(2**n):
            b = bin(i)[2:]
            buffer = ""
            if len(b) < len(nums):  # add zeros at LHS
                for _ in range(len(nums) - len(b)):
                    buffer += "0"
            if buffer:
                b = list(buffer + b)
            else:
                b = list(b)
            count = 0
            subset: list[int] = []
            while count < n:
                if b[count] == '1':
                    subset.append(nums[count])
                count += 1
            subsets.append(subset)
        return subsets


def canonical(subsets: list[list[int]]) -> set[tuple[int, ...]]:
    """
    Convert list-of-lists to a set of tuples for order-insensitive comparison.
    Sort elements inside each subset so that different orders of the same subset compare equal.
    """
    return set(tuple(sorted(s)) for s in subsets)


def run_test(nums, expected):
    """
    expected can be:
      - a list of lists: the exact expected subsets (order doesn't matter)
      - an int: expected number of subsets
      - None: infer basic correctness by checking count == 2**n and uniqueness
    """
    try:
        result = Solution().subsets(nums)

        if isinstance(expected, list):
            ok = canonical(result) == canonical(expected)
        elif isinstance(expected, int):
            ok = len(result) == expected and len(canonical(result)) == expected
        else:  # expected is None -> check count == 2**n and uniqueness
            expected_count = 1 << len(nums)
            ok = len(result) == expected_count and len(canonical(result)) == expected_count

        print(ok)
        if not ok:
            print(f"  nums:     {nums}")
            print(f"  expected: {expected}")
            shown = sorted(result, key=lambda s: (len(s), s))
            print(f"  got ({len(result)}): {shown}")
    except NotImplementedError as nie:
        print("NOT IMPLEMENTED ->", nie)
    except Exception as e:
        print(f"ERROR -> {e}")


def main() -> None:
    samples = [
        # Problem examples
        ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
        ([0], [[], [0]]),

        # Additional tests / edge cases
        ([], [[]]),                         # empty input -> only empty subset
        ([1], [[], [1]]),                   # single element
        ([1, 2], [[], [1], [2], [1, 2]]),   # two elements
        ([-1, 0, 1], None),                 # negative and positive, check count==8
        ([1, 2, 3, 4], None),               # 4 elements, check count==16
        (list(range(10)), None),            # max-size test (10 elements -> 1024 subsets)
    ]

    for nums, expected in samples:
        run_test(nums, expected)


if __name__ == "__main__":
    main()
