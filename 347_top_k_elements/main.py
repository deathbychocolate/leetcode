from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d: dict[int, int] = {}

        # count elements
        for num in nums:
            if not d.get(num):
                d[num] = 1
            else:
                d[num] += 1

        # sort by frequency
        d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

        return list(d.keys())[:k]


def main() -> None:
    r1: bool = [] == Solution().topKFrequent([1,1,1,2,2,3], k=2)
    r2: bool = [] == Solution().topKFrequent([1], k=1)
    r3: bool = [] == Solution().topKFrequent([1,2,1,2,1,2,3,1,3,2], k=2)
    print(r1)
    print(r2)
    print(r3)


if __name__ == "__main__":
    main()
