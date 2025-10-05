
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

def main() -> None:
    s1, t1 = "anagram", "nagaram"
    s2, t2 = "rat", "car"
    r1 = Solution().isAnagram(s=s1, t=t1)
    r2 = Solution().isAnagram(s=s2, t=t2)
    print(r1)  # Should be true.
    print(r2)  # Should be false.


if __name__=="__main__":
    main()
