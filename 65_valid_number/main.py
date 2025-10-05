"""https://leetcode.com/problems/valid-number/"""

from string import digits

ALLOWED_CHARS_SPECIAL = "e" + "E" + "-" + "+" + "."
ALLOWED_CHARS = digits + ALLOWED_CHARS_SPECIAL
ALLOWED_CHARS_SPECIAL_RHS = "-" + "+"
ALLOWED_CHARS_RHS = digits + ALLOWED_CHARS_SPECIAL_RHS

class Solution:
    def isNumber(self, s: str, is_rhs=False) -> bool:
        """A string is not a valid number if:

        - It contains only letters.
        - It contains a mix of letters and numbers (numbers on LHS).
        - It has an 'e' with only numbers only on LHS or only RHS.
        - It has a sign that is not on LHS.
        - It has a sign that on LHS, but is repeated.
        """

        if not any(char.isdigit() for char in s):
            return False

        for char in list(s):  # check if contains chars not in ALLOWED_CHARS
            if is_rhs:
                if char not in ALLOWED_CHARS_RHS:
                    return False
            if not is_rhs:
                if char not in ALLOWED_CHARS:
                    return False

        lhs, rhs = None, None
        is_number_lhs, is_number_rhs = None, None
        if "e" in s:  # check if uses 'e' correctly
            if s.count("e") > 1:
                return False
            if len(s.strip("e").split("e")) != 2:
                return False
            lhs, rhs = s.split("e")
        elif "E" in s:
            if s.count("E") > 1:
                return False
            if len(s.strip("E").split("E")) != 2:
                return False
            lhs, rhs = s.split("E")

        if not lhs and not rhs:
            if "+" in s or "-" in s:
                if not (
                    (s.startswith("+") or s.startswith("-")) and
                    (s.count("+") + s.count("-")) == 1
                ):
                    return False
            if s.count(".") > 1:
                return False
            return True

        is_number_lhs = self.isNumber(s=lhs, is_rhs=False)
        is_number_rhs = self.isNumber(s=rhs, is_rhs=True)

        return is_number_lhs and is_number_rhs


def main() -> None:
    valid = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", "-1E+3", ".1"]
    invalid = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", ".", "+", "-", "..2", "4e1.e"]
    result = False

    print("All values should be valid/True:")
    print("==========================================")
    for value in valid:
        result = Solution().isNumber(s=value)
        print(result)
    print()

    print("All values should be invalid/False:")
    print("==========================================")
    for value in invalid:
        result = Solution().isNumber(s=value)
        print(result)
    print()


if __name__=="__main__":
    main()
