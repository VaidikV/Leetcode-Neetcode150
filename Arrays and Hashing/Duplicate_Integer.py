nums = [1, 2, 3]


def hasduplicate(nums):
    hashset = set()
    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False

print(hasduplicate(nums))

# Alternate solutions
#1
# def containsDuplicate(self, nums: List[int]) -> bool:
#     return (len(set(nums)) != len(list(nums)))

#2
# def hasduplicate(nums):
#     n = len(nums)
#     for i in range(1, n):
#         if nums[i] == nums[i - 1]:
#             return True
#     return False



