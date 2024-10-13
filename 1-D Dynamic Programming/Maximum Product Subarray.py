def maxProduct(nums):
    res = max(nums)
    cur_min, cur_max = 1, 1

    for n in nums:
        if n == 0:
            cur_min, cur_max = 1, 1
            continue

        tmp = n * cur_max
        cur_max = max(tmp, n * cur_min, n)
        cur_min = min(tmp, n * cur_min, n)
        res = max(res, cur_max)
    return res

nums = [2,3,-2,4]
print(maxProduct(nums))

