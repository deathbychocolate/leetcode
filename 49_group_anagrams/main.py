from typing import List


class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        words_dict: dict[int, str] = {index: word for index, word in enumerate(words)}
        words_dict_sorted: dict[int, str] = {index: "".join(sorted(word)) for index, word in enumerate(words)}
        words_dict_sorted_sorted = dict(sorted(words_dict_sorted.items(), key=lambda item: item[1]))
        main_list: List[List[str]] = []
        child_list: List[str] = []
        for key, value in words_dict_sorted.items():
            if not child_list:
                child_list.append(value)
            elif value == child_list[0]:
                child_list.append(value)
            else:
                main_list.append(child_list)

        return [[""]]


def main() -> None:
    r1 = [["bat"],["nat","tan"],["ate","eat","tea"]] == Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    r2 = [[""]] == Solution().groupAnagrams([""])
    r3 = [["a"]] == Solution().groupAnagrams(["a"])
    print(r1)
    print(r2)
    print(r3)


if __name__ == "__main__":
    main()
