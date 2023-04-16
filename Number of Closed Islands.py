# https://leetcode.com/problems/number-of-closed-islands/


# first thought, dfs, TC:O(NM), SC:O(NM)
def closedIsland(grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])

    def dfs(i, j):
        # return True if all neighbors are 1 or 0, w/o boundary
        if not 0 <= i < n or not 0 <= j < m:
            return False
        if grid[i][j] == 1 or visited[i][j]:
            return True
        visited[i][j] = True
        if not all(
                [dfs(i + 1, j), dfs(i, j + 1), dfs(i - 1, j), dfs(i, j - 1)]):  # any nei out of bound => return False
            return False
        return True

    res = 0
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 or visited[i][j]:
                continue
            if dfs(i, j):
                res += 1
    return res