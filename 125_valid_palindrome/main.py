
class Solution:
    # More Pythonic Solution
    def isPalindrome(self, s: str) -> bool:
        s = "".join([c for c in s if c.isalpha() or c.isdigit()]).lower()
        return s == s[::-1]

    # # More Traditional Solution
    # import re
    # s = s.strip()
    # s = s.lower()
    # s = s.replace(' ', '')
    # s = re.sub('[^A-Za-z0-9 ]+', '', s)

    # l = len(s)
    # l_is_odd = l%2 == 1

    # if l == 0:
    #     return True

    # if l_is_odd:  # do this so that we do not have to check the middle char
    #     l = l - 1

    # length_to_check = l/2

    # index = 0
    # while index < length_to_check:
    #     if s[index] != s[len(s) - index -1]:
    #         return False
    #     index = index + 1

    # return True



def main() -> None:
    r1 = True == Solution().isPalindrome("A man, a plan, a canal: Panama")
    r2 = False == Solution().isPalindrome("race a car")
    r3 = True == Solution().isPalindrome(" ")
    r4 = False == Solution().isPalindrome("0P")

    print(r1)
    print(r2)
    print(r3)
    print(r4)

    return None


if __name__ == "__main__":
    main()
