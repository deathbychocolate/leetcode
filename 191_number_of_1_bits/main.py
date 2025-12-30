class Solution:
    def hammingWeight(self, n: int) -> int:
        # Bitwise Right shift solution.
        count: int = 0
        for _ in range(32):
            if n & 1 == 1:
                count += 1
            n = n >> 1
        return count


def run_test(n: int, expected: int) -> None:
    try:
        result = Solution().hammingWeight(n)
        ok = result == expected
        print(ok)
        if not ok:
            print(f"  n:        {n} (binary: {bin(n)})")
            print(f"  expected: {expected}")
            print(f"  got:      {result}")
    except Exception as e:
        print(f"ERROR -> {e}")


def main() -> None:
    samples = [
        # Problem examples
        (11, 3),  # 0b00000000000000000000000000001011
        (128, 1),  # 0b00000000000000000000000010000000
        (2147483645, 30),  # 0b01111111111111111111111111111101
        # Additional tests / edge cases
        (0, 0),
        (1, 1),
        (2, 1),
        (7, 3),  # 0b111
        (15, 4),  # 0b1111
        (2**31 - 1, 31),  # all 1s
    ]

    for n, expected in samples:
        run_test(n, expected)


if __name__ == "__main__":
    main()
