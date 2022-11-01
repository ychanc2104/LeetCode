# https://leetcode.com/problems/where-will-the-ball-fall/description/


# first thought, dfs, TC:O(MN), SC:O(N) N is number of rows, M is number of columns
def findBall(grid: List[List[int]]) -> List[int]:
    # ball can fall if right(1) or left(-1) is same dir
    def dfs(i, j):
        if j < 0 or j >= len(grid[0]): return -1
        if i == len(grid): return j
        if grid[i][j] == 1:
            if j == len(grid[0]) - 1 or grid[i][j] != grid[i][j + 1]: return -1
            return dfs(i + 1, j + 1)
        else:
            if j == 0 or grid[i][j] != grid[i][j - 1]: return -1
            return dfs(i + 1, j - 1)

    return [dfs(0, j) for j in range(len(grid[0]))]


# iterative dfs, TC:O(MN), SC:O(1) N is number of rows, M is number of columns
def findBall2(grid: List[List[int]]) -> List[int]:
    # ball can fall if right(1) or left(-1) is same dir
    res = []
    n, m = len(grid), len(grid[0])
    for c in range(m):
        for r in range(n):
            c_prev = c
            c += grid[r][c]
            if c < 0 or c >= m or grid[r][c] != grid[r][c_prev]:
                res.append(-1)
                break # do not go to else
        else:
            res.append(c)
    return res