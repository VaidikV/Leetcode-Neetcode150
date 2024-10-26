
def coin_change(coins, amount):
    # dp = [amount +  1] * (amount + 1)
    # dp[0] = 0
    #
    # for a in range(1, amount):
    #     for c in coins:
    #         if a - c >= 0:
    #             dp[a] = min(dp[a], 1 + dp[a-c])
    #
    # return dp[amount] if dp[amount] != amount + 1 else -1

    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])

    return dp[amount] if dp[amount] != amount + 1 else -1


coins = [1, 2, 4]
amount = 9
print(coin_change(coins, amount))

