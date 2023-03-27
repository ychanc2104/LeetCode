# https://leetcode.com/problems/minimum-path-sum/description/


# first thought, bottom-up dp, TC:O(NM), SC:O(NM)
def minPathSum(grid: List[List[int]]) -> int:
    # dp[i][j]: min path from 0,0 to i,j
    n, m = len(grid), len(grid[0])
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = grid[0][0]
    for i in range(n):
        for j in range(m):
            if (i, j) == (0, 0): continue
            dp[i][j] = min(dp[i][j - 1] if j > 0 else float('inf'), dp[i - 1][j] if i > 0 else float('inf')) + grid[i][
                j]
    return dp[-1][-1]


# space optimized bottom-up dp, TC:O(NM), SC:O(M)
def minPathSum2(grid: List[List[int]]) -> int:
    # dp[i][j]: min path from 0,0 to i,j
    n, m = len(grid), len(grid[0])
    dp = [0] * m
    dp[0] = grid[0][0]
    for i in range(n):
        for j in range(m):
            if (i,j) == (0,0): continue
            dp[j] = min(dp[j-1] if j > 0 else float('inf'), dp[j] if i > 0 else float('inf')) + grid[i][j]
    return dp[-1]