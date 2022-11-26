# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# first thought
def maxProfit(prices) -> int:
    L, R = 0, 1
    res = 0
    while R < len(prices):
        buy = prices[L]
        sell = prices[R]
        profit = sell - buy
        print(L, R, profit)
        if buy > sell:
            L = R
        R += 1
        # print(profit, L)
        res = max(res, profit)
    return res

# Kadane's algorithm
def maxProfit2(prices) -> int:
    cur, best = float("inf"), 0
    for i in range(len(prices)-1):
        cur = min(cur, prices[i])
        best = max(best, prices[i+1]-cur)
    return best

# Kadane's algorithm, dp
def maxProfit3(prices) -> int:
    sold = 0 # max to sold stock in [0,i]
    held = -prices[0] # max profit to hold stock in [0,i]
    for i in range(1, len(prices)):
        sold = max(sold, held + prices[i])
        held = max(held, -prices[i])
    return sold

prices = [7,1,5,3,6,4,10,0,19,0]

res = maxProfit(prices)
res2 = maxProfit2(prices)


