def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # base case: 0 coins to make amount 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
coins = [1, 2, 5]
amount = 11
print(coinChange(coins, amount))  # Output: 3 (5 + 5 + 1)
