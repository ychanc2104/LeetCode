# https://leetcode.com/problems/bomb-enemy/
# https://leetcode.com/problems/bomb-enemy/solutions/83387/Short-O(mn)-time-O(n)-space-solution/


# first thought, 2d dp, TC:O(NM*(N+M)), SC:O(NM)
def maxKilledEnemies(grid: List[List[str]]) -> int:
    n, m = len(grid), len(grid[0])
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            cell = grid[i][j]
            if cell == "E":
                for ro, co in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    rn, cn = i + ro, j + co
                    while 0 <= rn < n and 0 <= cn < m and grid[rn][cn] != "W":
                        dp[rn][cn] += 1 if grid[rn][cn] == "0" else 0
                        rn += ro
                        cn += co
    return max(c for row in dp for c in row)


# 1d dp, TC:O(3NM)~O(NM), SC:O(M)
def maxKilledEnemies(grid: List[List[str]]) -> int:
    n, m = len(grid), len(grid[0])
    row_counter = 0
    col_counter = [0] * m
    res = 0
    for i in range(n):
        for j in range(m):
            if j == 0 or grid[i][j-1] == 'W': # new row or previous col is a wall
                # scan whole cols
                row_counter = 0
                for k in range(j, m):
                    if grid[i][k] == 'W':
                        break
                    elif grid[i][k] == 'E':
                        row_counter += 1
            if i == 0 or grid[i-1][j] == 'W': # new col or previous row is a wall
                # scan whole rows
                col_counter[j] = 0
                for k in range(i, n):
                    if grid[k][j] == 'W':
                        break
                    elif grid[k][j] == 'E':
                        col_counter[j] += 1

            if cell == '0':
                res = max(res, row_counter + col_counter[j])

    return res