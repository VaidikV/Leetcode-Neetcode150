
def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1

    while l <= r:
        if numbers[l] + numbers[r] == target:
            return [l + 1, r + 1]
        elif numbers[l] + numbers[r] > target:
            r -= 1
        else:
            l += 1


    # for i, n in enumerate(numbers):
    #     diff = target - n
    #
    #     if diff in prev_map:
    #         return [prev_map[diff], i + 1]
    #
    #     prev_map[n] = i + 1


numbers = [2, 7, 11, 15]
target = 13

print(twoSum(numbers, target))
