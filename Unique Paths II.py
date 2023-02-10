# https://leetcode.com/problems/unique-paths-ii/description/

# bottom-up dp, TC:O(NM), SC:O(NM)
def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    n, m = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if obstacleGrid[i - 1][j - 1] == 1: continue
            if i == 1 and j == 1:
                dp[i][j] = 1 # initial value
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]


# bottom-up dp, TC:O(NM), SC:O(M)
def uniquePathsWithObstacles2(obstacleGrid: List[List[int]]) -> int:
    n, m = len(obstacleGrid), len(obstacleGrid[0])
    dp = [0] * (m+1)
    for i in range(1, n+1):
        for j in range(1, m+1):
            if obstacleGrid[i-1][j-1] == 1:
                dp[j] = 0
            elif i==1 and j==1:
                dp[j] = 1 # initial value
            else:
                dp[j] += dp[j-1]
    return dp[-1]