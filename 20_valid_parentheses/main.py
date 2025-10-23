class Solution:

    def isValid(self, s: str) -> bool:
        o: set[str] = {"(", "[", "{"}
        c: set[str] = {")", "]", "}"}
        c_o: dict[str, str] = {")": "(", "]": "[", "}": "{"}
        stack = []
        for ch in list(s):
            if ch in o:
                stack.append(ch)
            elif ch in c:
                # check if last character is correct complement, if so... pop
                if len(stack) < 1 or stack[-1] != c_o[ch]:
                    return False
                else:
                    stack.pop()

        return len(stack) == 0


def main() -> None:
    r1 = True == Solution().isValid(s="()")
    r2 = True == Solution().isValid(s="()[]{}")
    r3 = False == Solution().isValid(s="(]")
    r4 = True == Solution().isValid(s="([])")
    r5 = False == Solution().isValid(s="([)]")
    r6 = False == Solution().isValid(s="]")
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)
    print(r6)


if __name__ == "__main__":
    main()
