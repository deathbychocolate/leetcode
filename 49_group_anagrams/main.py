from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
        return list(groups.values())


# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         words = ["".join(sorted(word)) for word in strs]
#         hashes = list(set(words))
#         strs_words = sorted(zip(strs, words), key=lambda x: x[1])

#         groups: list[list[str]] = []
#         group: list[str] = []
#         for hash in hashes:
#             group = []
#             for strs_word in strs_words:
#                 if hash == strs_word[1]:
#                     group.append(strs_word[0])
#             groups.append(group)
#         return groups


def main() -> None:
    r1 = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]] == Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    r2 = [[""]] == Solution().groupAnagrams([""])
    r3 = [["a"]] == Solution().groupAnagrams(["a"])
    print(r1)
    print(r2)
    print(r3)


if __name__ == "__main__":
    main()
