class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) <= 1:
            return len(s)

        l: int = 0
        r: int = 1
        ln: int = 1
        sequence = {s[0]}
        while r < len(s):
            if s[r] not in sequence:
                sequence.add(s[r])
                if len(sequence) > ln:
                    ln = len(sequence)
                r += 1
            else:  # duplicate letter found
                sequence.remove(s[l])
                l += 1

        return ln


def main() -> None:
    r1 = 3 == Solution().lengthOfLongestSubstring(s="abcabcbb")
    r2 = 1 == Solution().lengthOfLongestSubstring(s="bbbbb")
    r3 = 3 == Solution().lengthOfLongestSubstring(s="pwwkew")
    r4 = 2 == Solution().lengthOfLongestSubstring(s="au")
    r5 = 2 == Solution().lengthOfLongestSubstring(s="aab")
    r6 = 3 == Solution().lengthOfLongestSubstring(s="dvdf")
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)
    print(r6)


if __name__ == "__main__":
    main()
