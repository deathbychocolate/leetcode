class Solution(object):
    def longestCommonPrefix(self, strs: list[str]) -> str:

        # Edge cases.
        if len(strs) < 1:
            return ""

        # Start from the smallest word first.
        strs.sort(key=len)
        lcp: str = strs[0]
        if lcp == "":
            return lcp

        lcp_new: str = ""
        for word in strs:
            for i, c in enumerate(list(word)):
                if i < len(lcp) and lcp[i] == c:
                    lcp_new += c
                else:
                    break
            if len(lcp_new) < len(lcp):
                if lcp_new == "" and lcp != "":
                    return lcp_new
                lcp = lcp_new
            lcp_new = ""

        return lcp


def main() -> None:
    r1 = "fl" == Solution().longestCommonPrefix(strs=["flower", "flow", "flight"])
    r2 = "" == Solution().longestCommonPrefix(strs=["dog", "racecar", "car"])
    r3 = "" == Solution().longestCommonPrefix(strs=["", "b"])
    r4 = "aa" == Solution().longestCommonPrefix(strs=["aaa", "aa", "aaa"])
    r5 = "a" == Solution().longestCommonPrefix(strs=["a"])
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)


if __name__ == "__main__":
    main()
