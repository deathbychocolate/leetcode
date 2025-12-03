class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

        # index: int = 0
        # while index <= len(haystack) - len(needle):
        #     if haystack.startswith(needle, index):
        #         return index
        #     index += 1
        # return -1


def main() -> None:
    r1 = 0 == Solution().strStr(haystack = "sadbutsad", needle = "sad")
    r2 = -1 == Solution().strStr(haystack = "leetcode", needle = "leeto")
    r3 = 0 == Solution().strStr(haystack = "a", needle = "a")
    print(r1)
    print(r2)
    print(r3)


if __name__ == "__main__":
    main()
