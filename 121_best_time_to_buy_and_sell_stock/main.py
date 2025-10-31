from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0

        l: int = 0
        r: int = 1
        net: int = 0
        net_max: int = 0
        while r < len(prices):
            net = prices[r] - prices[l]
            if net > net_max:
                net_max = net
                r += 1
            elif net <= net_max:
                if prices[l] > prices[r]:
                    l += 1
                    r = l + 1
                else:
                    r += 1

        return net_max


def main() -> None:
    r1 = 5 == Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4])
    r2 = 0 == Solution().maxProfit(prices=[7, 6, 4, 3, 1])
    r3 = 1 == Solution().maxProfit(prices=[1, 2])
    print(r1)
    print(r2)
    print(r3)


if __name__ == "__main__":
    main()
