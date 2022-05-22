# https://leetcode.com/problems/coin-change/

## TC: O(amount*len(coins))
def coinChange(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return -1 if dp[amount] == amount + 1 else dp[amount]


## faster with assign dp[coin]
def coinChange2(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if a == c:
                dp[a] = 1
            elif a - c > 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return -1 if dp[amount] == amount + 1 else dp[amount]

coins = [1,2,5]
amount = 11
res = coinChange(coins, amount)
res2 = coinChange2(coins, amount)