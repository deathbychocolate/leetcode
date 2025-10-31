from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0

        l: int = 0
        r: int = 1
        net: int = 0
        net_total: int = 0

        while r < len(prices):
            net = prices[r] - prices[l]
            if net > 0:
                net_total += net
            l += 1
            r = l + 1

        return net_total


def main() -> None:
    r1 = 7 == Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4])
    r2 = 4 == Solution().maxProfit(prices=[1, 2, 3, 4, 5])
    r3 = 0 == Solution().maxProfit(prices=[7, 6, 4, 3, 1])
    r4 = 3 == Solution().maxProfit(prices=[2, 2, 5])
    print(r1)
    print(r2)
    print(r3)
    print(r4)


if __name__ == "__main__":
    main()
