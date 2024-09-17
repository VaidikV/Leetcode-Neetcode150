

def max_profit(prices):
    l, r = 0, 1
    max_p = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_p = max(max_p, profit)
        else:
            l = r
        r += 1
    return max_p


prices = [7,1,5,3,6,4]
print(max_profit(prices))

