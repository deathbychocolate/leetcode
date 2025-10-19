from typing import List
import bisect


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # check edge cases
        if len(nums) < 2:
            return len(nums)

        # remove duplicates
        nums_uniq: list[int] = list(set(nums))

        # bisect.insort() O(n) vs sorted() O(n^2)
        nums_uniq_sorted: list[int] = []
        for num in nums_uniq:
            bisect.insort(nums_uniq_sorted, num)

        # find max consecutive length
        count: int = 0
        max_count: int = 0
        cur_num: int | None = None
        for num in nums_uniq_sorted:
            if cur_num is None or num != cur_num + 1:
                count = 1
            else:
                count += 1
            cur_num = num

            if count > max_count:
                max_count = count

        return max_count


def main() -> None:
    r1 = 4 == Solution().longestConsecutive(nums=[100, 4, 200, 1, 3, 2])
    r2 = 9 == Solution().longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
    r3 = 3 == Solution().longestConsecutive(nums=[1, 0, 1, 2])
    r4 = 7 == Solution().longestConsecutive(nums=[9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6])
    print(r1)
    print(r2)
    print(r3)
    print(r4)


if __name__ == "__main__":
    main()
