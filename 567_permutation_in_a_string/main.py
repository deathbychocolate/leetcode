from itertools import permutations


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Algorithmically sound, but runs into 'Memory Limit Exceeded' error.
        if not s1 or not s2:
            return False

        perm: list[str] = ["".join(x) for x in permutations(s1)]

        for p in perm:
            if p in s2:
                return True

        return False


def main() -> None:
    r1 = True == Solution().checkInclusion(s1="ab", s2="eidbaooo")
    r2 = False == Solution().checkInclusion(s1="ab", s2="eidboaoo")
    print(r1)
    print(r2)


if __name__ == "__main__":
    main()
