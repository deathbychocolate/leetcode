
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


def main() -> None:
    nums1 = [1,2,3,1]
    nums2 = [1,2,3,4]
    nums3 = [1,1,1,3,3,4,3,2,4,2]
    r1 = Solution().containsDuplicate(nums=nums1)
    r2 = Solution().containsDuplicate(nums=nums2)
    r3 = Solution().containsDuplicate(nums=nums3)
    print(r1)  # Should be true.
    print(r2)  # Should be false.
    print(r3)  # Should be true.


if __name__=="__main__":
    main()
