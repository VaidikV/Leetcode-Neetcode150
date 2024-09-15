# I did this all by myself so super proud.

def maxArea(height):
    res = []
    l = 0
    r = len(height) - 1

    while l < r:
        if height[l] < height[r]:
            res.append(height[l] * (r - l))
            l += 1
        else:
            res.append(height[r] * (r - l))
            r -= 1

    return max(res)


height = [1,8,6,2,5,4,8,3,7]

print(maxArea(height))