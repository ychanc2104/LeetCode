# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/78334/Python-solution-memoization-dp-288ms
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/2052360/Python%3A-Beginner-Friendly-%22Recursion-to-DP%22-Intuition-Explained

# dp method, cost more RAM because of dict, TC:O(MN), SC:O(MN)
def longestIncreasingPath(matrix) -> int:
    def dfs(row, col):
        if (row, col) in memo:
            return memo[(row, col)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if r < 0 or r >= n or c < 0 or c >= m or matrix[row][col] >= matrix[r][c]:
                continue
            memo[(row, col)] = max(memo.get((row, col), 1), dfs(r, c) + 1)
        return memo.setdefault((row, col), 1)

    memo = {}
    n, m = len(matrix), len(matrix[0])
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    res = 0
    for i in range(n):
        for j in range(m):
            res = max(res, dfs(i, j))
    print(memo)
    return res

def longestIncreasingPath2(matrix) -> int:
    def dfs(i, j):
        if not dp[i][j]:
            val = matrix[i][j]
            dp[i][j] = 1 + max(
                dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
        return dp[i][j]

    if not matrix or not matrix[0]: return 0
    M, N = len(matrix), len(matrix[0])
    dp = [[0] * N for i in range(M)]
    return max(dfs(x, y) for x in range(M) for y in range(N))



def longestIncreasingPath3(matrix) -> int:
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


def longestIncreasingPath4(matrix) -> int:
    def dfs(row, col, prev):
        if row < 0 or row >= n or col < 0 or col >= m or prev >= matrix[row][col]:
            return 0
        if dp[row][col] != 0:
            return dp[row][col]
        val = matrix[row][col]
        bottom = dfs(row - 1, col, val)
        left = dfs(row, col - 1, val)
        up = dfs(row + 1, col, val)
        right = dfs(row, col + 1, val)
        dp[row][col] = 1 + max(bottom, left, up, right)
        return dp[row][col]

    n, m = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(m)] for _ in range(n)]
    res = 0
    for i in range(n):
        for j in range(m):
            res = max(res, dfs(i, j, -1))
    return res


matrix = [[9,9,4],[6,6,8],[2,1,1]]
res = longestIncreasingPath(matrix)