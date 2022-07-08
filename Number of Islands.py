# https://leetcode.com/problems/number-of-islands/

# first thought, dfs, TC:O(N*M), SC:O(N*M)
def numIslands(grid) -> int:
    res = 0
    visit = set()

    def dfs(r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
            return
        if (r, c) in visit:
            return
        if grid[r][c] == "0":
            return
        visit.add((r, c))
        for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(r + y, c + x)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1" and (i, j) not in visit:
                res += 1
                dfs(i, j)
    return res


# dfs, mark visit as "0" to save visit, TC:O(N*M), SC:O(N*M), worst case for all lands
def numIslands(grid) -> int:
    res = 0
    def dfs(r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
            return
        grid[r][c] = "0"
        for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(r + y, c + x)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                res += 1
                dfs(i, j)
    return res
