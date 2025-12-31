class Solution:
    def countBits(self, n: int) -> list[int]:
        # Optimal. Uses previously computed numbers.
        # Looked up via i >> 1 (initialized with number 0 [bin form is 0]).
        result = [0] * (n + 1)
        for i in range(1, n + 1):
            result[i] = result[i >> 1] + (i & 1)
        return result

        # # Better.
        # result: list[int] = []
        # for num in range(n+1):
        #     count: int = 0
        #     while num:
        #         if num & 1 == 1:
        #             count += 1
        #         num = num >> 1
        #     result.append(count)
        # return result

        # # Naive solution: Recount all the bits with each number.
        # result: list[int] = []
        # for num in range(n+1):
        #     count: int = 0
        #     for _ in range(32):
        #         if num & 1 == 1:
        #             count += 1
        #         num = num >> 1
        #     result.append(count)
        # return result


def run_test(n: int, expected: list[int]) -> None:
    try:
        result = Solution().countBits(n)
        ok = result == expected
        print(ok)
        if not ok:
            print(f"  n:        {n}")
            print(f"  expected: {expected}")
            print(f"  got:      {result}")
    except Exception as e:
        print(f"ERROR -> {e}")


def main() -> None:
    samples = [
        # Problem examples
        (2, [0, 1, 1]),  # 0b0, 0b1, 0b10
        (5, [0, 1, 1, 2, 1, 2]),  # 0b0, 0b1, 0b10, 0b11, 0b100, 0b101
        # Additional tests / edge cases
        (0, [0]),
        (1, [0, 1]),
        (3, [0, 1, 1, 2]),  # 0b0, 0b1, 0b10, 0b11
        (7, [0, 1, 1, 2, 1, 2, 2, 3]),  # 0b0 to 0b111
        (15, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]),  # 0b0 to 0b1111
    ]

    for n, expected in samples:
        run_test(n, expected)


if __name__ == "__main__":
    main()
