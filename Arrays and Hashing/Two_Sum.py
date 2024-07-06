from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    prev_map = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i


numz = [2, 4, 3, 7]
targetz = 5
print(two_sum(numz, targetz))
# hashmap = {}
# nums = [2,4,3,7]
# target = 5
# for i, n in enumerate(nums):
#     diff = target - n
#     print(i,n,diff)
#     if diff in hashmap:
#         print(hashmap[diff], i)
#         break
#     hashmap[n] = i
#
# print(hashmap)