# https://leetcode.com/problems/minimum-cost-for-tickets/


# first thought, bottom-up dp, TC:O(N^2), SC:O(N)
def mincostTickets(days: List[int], costs: List[int]) -> int:
    n = len(days)
    dp = [0] * (n + 1)  # dp[i]: min cost days[:i+1]
    tickets = [(7, costs[1]), (30, costs[2])]
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + costs[0]  # baseline to use 1-day pass
        for j in range(1, i + 1):  # dp[i] = min(dp[i], dp[j] + c)
            for d, c in tickets:
                if days[i - 1] - days[j - 1] + 1 <= d:  # can use this
                    dp[i] = min(dp[i], dp[j - 1] + c)
    # print(dp)
    return dp[-1]


# bottom-up dp, TC:O(M), M is max in days, SC:O(M)
def mincostTickets2(days: List[int], costs: List[int]) -> int:
    n = days[-1]
    dp = [0] + [float('inf')] * (n) # dp[i]: min cost at day i
    days_set = set(days)
    durations = [1, 7, 30]
    for i in range(1, n+1):
        if i in days_set:
            for d,c in zip(durations, costs):
                dp[i] = min(dp[i], dp[max(i-d, 0)]+c)
        else:
            dp[i] = dp[i-1]
    return dp[-1]