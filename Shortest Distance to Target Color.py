# https://leetcode.com/problems/shortest-distance-to-target-color/


# first thought, dp, TC:O(), SC:()
def shortestDistanceColor(colors: List[int], queries: List[List[int]]) -> List[int]:
    n = len(colors)
    dp = [[float('inf')] * 4 for _ in range(n)]
    for i in range(n):
        if i > 0:
            dp[i] = [d + 1 for d in dp[i - 1]]
        dp[i][colors[i]] = 0

    for i in range(n - 1, -1, -1):
        if i < n - 1:
            dp[i] = [min(dp[i][j], dp[i + 1][j] + 1) for j in range(4)]
        dp[i][colors[i]] = 0

    return [dp[i][c] if dp[i][c] != float('inf') else -1 for i, c in queries]