# def num_bits(n):
#     ans = 0
#     while n:
#         ans += n % 2
#         n = n >> 1
#     return ans


# Alt solution
def num_bits(n):
    ans = 0
    while n:
        n = n & (n - 1)
        ans += 1
    return ans

bin_no = 2147483645
print(num_bits(bin_no))