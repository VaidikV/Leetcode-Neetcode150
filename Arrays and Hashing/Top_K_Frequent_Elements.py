# My solution

from typing import List
from collections import defaultdict

numbers = [4, 1, -1, 2, -1, 2, 3]
top = 2


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    sol = []
    hashmap = defaultdict(int)

    for n in nums:
        hashmap[n] += 1

    sortedhash = sorted(hashmap.items(), key=lambda kv: kv[1], reverse=True)
    print(sortedhash)
    for i in range(k):
        sol.append(sortedhash[i][0])

    return sol


print(top_k_frequent(numbers, top))


# Neetcode Solution

# from typing import List
#
# nums = [1, 3, 5, 1, 2, 3, 3]
# k = 2
#
#
# def topKFrequent(nums: List[int], k: int) -> List[int]:
#     count = {}
#     freq = [[] for i in range(len(nums) + 1)]
#     for n in nums:
#         count[n] = 1 + count.get(n, 0)
#
#     for n, c in count.items():
#         freq[c].append(n)
#
#     print(count)
#     print(freq)
#
#     res = []
#
#     for i in range(len(freq) - 1, 0, -1):
#         print(i)
#         for n in freq[i]:
#             res.append(n)
#             if len(res) == k:
#                 return res
#
#
# print(topKFrequent(nums, k))
