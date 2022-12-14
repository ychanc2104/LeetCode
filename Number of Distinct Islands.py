# https://leetcode.com/problems/number-of-distinct-islands/
# https://leetcode.com/problems/number-of-distinct-islands/solutions/108480/simple-python-169ms/

# dfs to find the shape of each island, TC:O(NM), SC:O(NM)
def numDistinctIslands(grid: List[List[int]]) -> int:
    # use relative position of every island
    def dfs(ref: list, i, j):
        # ref is top-left point
        if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0 or visited[i][j]:
            return
        visited[i][j] = True
        shape.append((i - ref[0], j - ref[1]))  # add relative position
        for ro, co in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            dfs(ref, i + ro, j + co)

    n, m = len(grid), len(grid[0])
    visited = [[False] * m for _ in range(n)]
    res = set()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0 or visited[i][j]:
                continue
            shape = []
            dfs((i, j), i, j)
            res.add(tuple(shape)) # or res.add(frozenset(shape))
    return len(res)