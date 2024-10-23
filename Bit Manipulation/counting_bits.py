# def count_bits(n):
#     ans = []
#
#     for i in range(n + 1):
#         max_one = 0
#         while i:
#             i &= (i -1)
#             max_one += 1
#         ans.append(max_one)
#     return ans




# alt solution using dp

def count_bits(n):
    dp = [0] * (n+1)
    offset = 1

    for i in range(1, n + 1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]

    return dp

num = 5
print(count_bits(num))