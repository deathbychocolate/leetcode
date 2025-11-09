from typing import List
from collections import Counter
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort - O(n) [usually] - Worst case O(n^2) if all numbers are equal and is a large list.
        d: defaultdict[int, int] = defaultdict(int)
        for num in nums:
            d[num] += 1

        buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]
        for num, count in d.items():
            buckets[count].append(num)

        result: list[int] = []
        index: int = len(buckets) - 1
        while index >= 0:
            for num in buckets[index]:
                result.append(num)
                if len(result) == k:
                    return result
            index -= 1

        return []

        # Heap - O(klog(n))
        # return [num for num, _ in Counter(nums).most_common(k)]

        # Hash - O(n) + O(nlogn) for sorting
        # d: dict[int, int] = {}

        # # count elements
        # for num in nums:
        #     if not d.get(num):
        #         d[num] = 1
        #     else:
        #         d[num] += 1

        # # sort by frequency
        # d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

        # return list(d.keys())[:k]


def main() -> None:
    r1: bool = [1, 2] == Solution().topKFrequent([1, 1, 1, 2, 2, 3], k=2)
    r2: bool = [1] == Solution().topKFrequent([1], k=1)
    r3: bool = [1, 2] == Solution().topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], k=2)
    print(r1)
    print(r2)
    print(r3)


if __name__ == "__main__":
    main()
