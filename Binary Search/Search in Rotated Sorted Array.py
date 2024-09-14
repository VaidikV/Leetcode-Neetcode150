

def search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2
        if target == nums[m]:
            return m

        # left sorted portion
        if nums[l] <= nums[m]:
            if target > nums[m] or target < nums[l]:
                l = m + 1
            else:
                r = m - 1
        # if in right sorted portion
        else:
            if target < nums[m] or target > nums[r]:
                r = m - 1
            else:
                l = m + 1
    return -1


nums = [4, 5, 6, 7, 0, 1, 2]

print(search(nums, 5))

