class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b & mask != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return a & mask if b > mask else a


def run_test(a: int, b: int, expected: int) -> None:
    try:
        result = Solution().getSum(a, b)
        ok = result == expected
        print(ok)
        if not ok:
            print(f"  a:        {a}")
            print(f"  b:        {b}")
            print(f"  expected: {expected}")
            print(f"  got:      {result}")
    except Exception as e:
        print(f"ERROR -> {e}")


def main() -> None:
    samples = [
        # Problem examples
        (1, 2, 3),
        (2, 3, 5),
        # Additional tests / edge cases
        (0, 0, 0),
        (0, 5, 5),
        (5, 0, 5),
        (-1, 1, 0),
        (-5, 5, 0),
        (10, -5, 5),
        (-10, -5, -15),
        (100, 200, 300),
    ]

    for a, b, expected in samples:
        run_test(a, b, expected)


if __name__ == "__main__":
    main()
