from typing import List


def search(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l + r) // 2
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
    return -1


numss = [-1, 0, 3, 5, 9, 12]
targett = -1

print(search(numss, targett))
