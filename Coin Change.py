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


## TC: O((amount-1)*len(coins)) faster with assign dp[coin]
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

## dfs, (time exceed)
def coinChange3(coins, amount):

    coins.sort(reverse=True)
    min_coins = float('inf')
    def count_coins(start_coin, coin_count, remaining_amount):
        nonlocal min_coins
        if remaining_amount == 0:
            min_coins = min(min_coins, coin_count)
            return

        # Iterate from largest coins to smallest coins
        for i in range(start_coin, len(coins)):
            remaining_coin_allowance = min_coins - coin_count
            max_amount_possible = coins[i] * remaining_coin_allowance
            # print(coins[i],min_coins,coin_count,remaining_coin_allowance, max_amount_possible)
            if coins[i] <= remaining_amount and remaining_amount < max_amount_possible:
            # if coins[i] <= remaining_amount < max_amount_possible:
                count_coins(i, coin_count + 1, remaining_amount - coins[i])
    count_coins(0, 0, amount)
    return min_coins if min_coins < float('inf') else -1


## bfs, (the fastest)
def coinChange4(coins, amount):
    if amount == 0:
        return 0
    queue = [[0, 0]]
    visited = {0}
    step = 0
    for node, step in queue:
        for coin in coins:
            if node + coin in visited:
                continue
            if node + coin == amount:
                return step + 1
            elif node + coin < amount:
                queue.append([node + coin, step + 1])
                visited.add(node + coin)
    return -1

coins = [1,2,5]
amount = 11
res = coinChange(coins, amount)
res2 = coinChange2(coins, amount)