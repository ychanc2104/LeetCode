# https://leetcode.com/problems/minimum-falling-path-sum/description/


# first thought dp, TC:O(N^2), SC:O(N^2)
def minFallingPathSum(matrix: List[List[int]]) -> int:
    # dp from bottom
    n = len(matrix)
    dp = {(i, j): float('inf') for i in range(n) for j in range(n)}
    max_int = float('inf')
    for i in range(n - 1, -1, -1):  # from bottom
        for j in range(n - 1, -1, -1):  # from rightmost
            if i == n - 1:
                dp[(i, j)] = matrix[i][j]
            else:
                dp[(i, j)] = matrix[i][j] + min(dp.get((i + 1, j), max_int), dp.get((i + 1, j + 1), max_int),
                                                dp.get((i + 1, j - 1), max_int))
    return min(dp[(0, j)] for j in range(n))