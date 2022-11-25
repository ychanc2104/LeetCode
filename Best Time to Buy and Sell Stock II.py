# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# first thought dp, TC:O(N), SC:O(N)
def maxProfit(prices: List[int]) -> int:
    # dp[i]: res ending with index i
    dp = [0] * len(prices)
    for i in range(1, len(prices)):
        dp[i] = dp[i - 1] + max(0, prices[i] - prices[i - 1])
    return dp[-1]

# space optimized dp, TC:O(N), SC:O(1)
def maxProfit(self, prices: List[int]) -> int:
    # dp[i]: res ending with index i
    prevProfit = 0
    for i in range(1,len(prices)):
        prevProfit += max(0, prices[i] - prices[i-1])
    return prevProfit