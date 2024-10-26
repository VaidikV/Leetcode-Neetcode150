def reverseBits(n):
    # res = 0
    #
    # for i in range(32):
    #     res = res << 1 # right shift eg. 0 -> 00
    #     bit = n % 2 # extract least (rightmost bit) eg 101 -> 1
    #     res += bit
    #     n = n >> 1
    #
    # return res

    res = 0
    for i in range(32):
        res = res << 1
        bit = n % 2
        res += bit
        n = n >> 1

    return res

print(reverseBits(11111111111111111111111111111101))