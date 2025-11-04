from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        l: int = 0
        r: int = len(height) - 1
        area: int = 0
        area_max: int = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            if area > area_max:
                area_max = area
            elif height[l] >= height[r]:
                r -= 1
            elif height[l] < height[r]:
                l += 1
            else:
                print("A condition you did not account for occurred.")

        return area_max

        # i: int = 0
        # j: int = 0
        # h: int = 0
        # h_max: int = 0
        # while i < len(height):
        #     while j < len(height):
        #         h = min(height[i], height[j]) * abs(i - j)
        #         if h > h_max:
        #             h_max = h
        #         j += 1
        #     i += 1
        #     j = 0

        # return h_max


def main() -> None:
    r1 = 49 == Solution().maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7])
    r2 = 1 == Solution().maxArea(height=[1, 1])
    print(r1)
    print(r2)


if __name__ == "__main__":
    main()
