# https://leetcode.com/problems/maximal-square/


# first thought, TC:O(MNk), k is area of max square, TC:O(1)
def maximalSquare(matrix) -> int:
    def check(pos: list, size: int):
        y, x = pos
        if matrix[y][x] == "0" or y + size > len(matrix) or x + size > len(matrix[0]):
            return False
        for i in range(y, y + size):
            for j in range(x, x + size):
                if matrix[i][j] == "0":
                    return False
        return True

    res = 0
    n, m = len(matrix), len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            size = 1
            if min(n - i, m - j) ** 2 > res:  # possible area > res
                while check([i, j], size):
                    size += 1
            res = max(res, (size - 1)**2)
    return res

# 2d dp, TC:O(MN), SC:O(MN)
def maximalSquare2(matrix) -> int:
    if not matrix:
        return 0
    nrows = len(matrix)
    ncols = len(matrix[0])
    max_square_len = 0
    # dp[i][j]: side length of max square and (i,j) bottom right corner
    dp = [[0] * (ncols+1) for i in range(nrows+1)]
    # relation: dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    maxLen = 0
    for i in range(1,nrows+1):
        for j in range(1,ncols+1):
            if matrix[i-1][j-1] == "1":
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                maxLen = max(maxLen, dp[i][j])
    return maxLen ** 2


# 1d dp, TC:O(MN), SC:O(M)
def maximalSquare3(matrix) -> int:
    if not matrix:
        return 0
    nrows = len(matrix)
    ncols = len(matrix[0])
    max_square_len = 0
    # dp[i][j]: side length of max square and (i,j) bottom right corner
    dp = [0] * (ncols + 1)
    # relation: dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    maxLen = 0
    prev = 0
    for i in range(1, nrows + 1):
        for j in range(1, ncols + 1):
            temp = dp[j]  # (dp[i-1][j] in 2D dp)
            if matrix[i - 1][j - 1] == "1":
                dp[j] = min(dp[j], dp[j - 1], prev) + 1
                maxLen = max(maxLen, dp[j])
            else:
                dp[j] = 0
            prev = temp  # (dp[i-1][j-1] in 2D dp)
    return maxLen ** 2


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]


res = maximalSquare(matrix)