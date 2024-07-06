from typing import List
from collections import defaultdict

strings = ["eat", "tea", "tan", "ate", "nat", "bat"]


def group_anagrams(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)  # mapping char count to list of anagrams

    for s in strs:
        count = [0] * 26  # a to z

        for c in s:
            count[ord(c) - ord("a")] += 1  # here [ord(c) - ord("a")] == index of consonant in count

        res[tuple(count)].append(s)

    return list(res.values())


print(group_anagrams(strings))

# for s in strings:
#     count = [0] * 26
#     for c in s:
#         count[ord(c) - ord("a")] += 1
#
# print(count)

