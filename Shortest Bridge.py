# https://leetcode.com/problems/shortest-bridge/
# https://leetcode.com/problems/shortest-bridge/solutions/3546474/python-java-c-simple-solution-easy-to-understand/

import collections

# DFS+BFS, TC:O(N^2), SC:O(N^2)
def shortestBridge(grid: List[List[int]]) -> int:
    n = len(grid)
    queue = collections.deque()
    visited = [[False] * n for _ in range(n)]

    def dfs(r, c):
        if visited[r][c]:
            return
        visited[r][c] = True
        queue.append((r, c))
        for rn, cn in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)):
            if not 0 <= rn < n or not 0 <= cn < n or grid[rn][cn] == 0 or visited[rn][cn]:
                continue
            dfs(rn, cn)

    # DFS to find first island
    for i in range(n):
        for j in range(n):
            if grid[i][j] and not queue:
                dfs(i, j)

    # BFS to find another island
    res = 0
    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()
            for rn, cn in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)):
                if not 0 <= rn < n or not 0 <= cn < n or visited[rn][cn]:
                    continue
                if grid[rn][cn] and not visited[rn][cn]:
                    return res
                visited[rn][cn] = True
                queue.append((rn, cn))
        res += 1
