# https://leetcode.com/problems/max-area-of-island/description/

# dfs to count area, TC:O(NM), SC:O(NM)
def maxAreaOfIsland(grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])

    def dfs(r, c):
        if r < 0 or c < 0 or r >= n or c >= m or grid[r][c] == 0:
            return
        grid[r][c] = 0
        area[0] += 1
        for ro, co in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            dfs(r + ro, c + co)

    res = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0: continue
            area = [0]
            dfs(i, j)
            res = max(res, area[0])
    return res


def maxAreaOfIsland2(grid: List[List[int]]) -> int:

    n, m = len(grid), len(grid[0])
    def dfs(r, c):
        if r < 0 or c < 0 or r >= n or c >= m or grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        s = 1 # length of path
        for ro, co in ((1,0),(0,1),(-1,0),(0,-1)):
            s += dfs(r+ro, c+co)
        return s
    res = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0: continue
            res = max(res, dfs(i, j))
    return res