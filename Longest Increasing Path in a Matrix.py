# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/78334/Python-solution-memoization-dp-288ms
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/2052360/Python%3A-Beginner-Friendly-%22Recursion-to-DP%22-Intuition-Explained

# dp method, cost more RAM because of dict, TC:O(MN), SC:O(MN)
def longestIncreasingPath(matrix) -> int:
    n, m = len(matrix), len(matrix[0])
    dp = {}

    def helper(i, j):  # return longest length start from (i,j)
        if (i, j) in dp:
            return dp[(i, j)]
        res = 1
        for ro, co in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            rn, cn = i + ro, j + co
            if not 0 <= rn < n or not 0 <= cn < m or matrix[i][j] <= matrix[rn][cn]:
                continue
            res = max(res, helper(rn, cn) + 1)
        dp[(i, j)] = res
        return res

    res = 1
    for i in range(n):
        for j in range(m):
            res = max(res, helper(i, j))
    return res



def longestIncreasingPath2(matrix) -> int:
    def dfs(row, col):
        if dp[row][col] != 0:
            return dp[row][col]
        value = matrix[row][col]
        dp[row][col] = 1 + max(
            dfs(row + 1, col) if row + 1 < n and value < matrix[row + 1][col] else 0,
            dfs(row - 1, col) if row - 1 >= 0 and value < matrix[row - 1][col] else 0,
            dfs(row, col + 1) if col + 1 < m and value < matrix[row][col + 1] else 0,
            dfs(row, col - 1) if col - 1 >= 0 and value < matrix[row][col - 1] else 0)
        return dp[row][col]

    n, m = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(m)] for _ in range(n)]
    res = 0
    for i in range(n):
        for j in range(m):
            res = max(res, dfs(i, j))
    return res





matrix = [[9,9,4],[6,6,8],[2,1,1]]
res = longestIncreasingPath(matrix)