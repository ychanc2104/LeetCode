# https://leetcode.com/problems/number-of-enclaves/description/
# https://leetcode.com/problems/number-of-enclaves/solutions/265534/python-clean-dfs-solution/


# dfs, TC:O(NM), SC:O(NM)
def numEnclaves(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])

    def dfs(r, c):
        if not 0 <= r < m or not 0 <= c < n:
            return float('-inf')
        if grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        res = dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1) + 1
        return res

    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                continue
            temp = dfs(i, j)
            if temp != float('-inf'):
                res += temp
    return res