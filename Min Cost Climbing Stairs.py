# https://leetcode.com/problems/min-cost-climbing-stairs/description/

# bottom-up dp, TC:O(n), SC:O(n)
def minCostClimbingStairs(cost: List[int]) -> int:
    dp = [0] * (len(cost) + 1)  # dp[i]: how many costs to reach i
    for i in range(2, len(cost) + 1):
        take_one = dp[i - 1] + cost[i - 1]
        take_two = dp[i - 2] + cost[i - 2]
        dp[i] = min(take_one, take_two)
    return dp[-1]

# top-down dp, TC:O(n), SC:O(n)
def minCostClimbingStairs2(cost: List[int]) -> int:
    dp = {0:0, 1:0}
    def dfs(i):
        if i in dp:
            return dp[i]
        dp[i] = min(dfs(i-1) + cost[i-1], dfs(i-2) + cost[i-2])
        return dp[i]
    return dfs(len(cost))


# constant space bottom-up dp, TC:O(n), SC:O(1)
def minCostClimbingStairs3(cost: List[int]) -> int:
    n = len(cost)
    f0 = 0
    f1 = 0
    for i in range(2, n+1):
        take_one = f1 + cost[i-1]
        take_two = f0 + cost[i-2]
        f2 = min(take_one, take_two)
        f0, f1 = f1, f2
    return f1