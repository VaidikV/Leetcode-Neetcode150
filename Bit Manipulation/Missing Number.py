
def missingNumber(nums):
    n = len(nums)
    total = (n * (n+1))//2
    nums_sum = sum(nums)
    return total - nums_sum





nums = [0, 1]
print(missingNumber(nums))