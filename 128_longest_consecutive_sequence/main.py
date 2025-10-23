from typing import List

# import bisect


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # check edge cases
        if len(nums) < 2:
            return len(nums)

        nums_set: set[int] = set(nums)

        count: int = 1
        max_count: int = 1
        for num in nums_set:
            if num - 1 not in nums_set:  # start counting only if no previous num in sequence
                cur = num
                count = 1
                while cur + 1 in nums_set:
                    cur += 1
                    count += 1
                if count > max_count:
                    max_count = count

        return max_count

        # # check edge cases
        # if len(nums) < 2:
        #     return len(nums)

        # # remove duplicates
        # nums_uniq: list[int] = sorted(set(nums))

        # # find max consecutive length
        # count: int = 0
        # max_count: int = 0
        # cur_num: int | None = None
        # for num in nums_uniq:
        #     if cur_num is None or num != cur_num + 1:
        #         count = 1
        #     else:
        #         count += 1
        #     cur_num = num

        #     if count > max_count:
        #         max_count = count

        # return max_count


def main() -> None:
    r1 = 4 == Solution().longestConsecutive(nums=[100, 4, 200, 1, 3, 2])
    r2 = 9 == Solution().longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
    r3 = 3 == Solution().longestConsecutive(nums=[1, 0, 1, 2])
    r4 = 7 == Solution().longestConsecutive(nums=[9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6])
    r5 = 3 == Solution().longestConsecutive(nums=[1, 0, -1])
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)


if __name__ == "__main__":
    main()
