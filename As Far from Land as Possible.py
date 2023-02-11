# https://leetcode.com/problems/as-far-from-land-as-possible/
# https://leetcode.com/problems/as-far-from-land-as-possible/solutions/422691/7ms-dp-solution-with-example-beats-100/

import collections


# do BFS from all lands at a time, TC:O(N^2), SC:O(N^2)
def maxDistance(grid: List[List[int]]) -> int:
    def bfs(queue):
        # visited = set()
        dist = -1
        while queue:
            r, c, dist = queue.popleft()
            for ro, co in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                rn, cn = r + ro, c + co
                if not 0 <= rn < n or not 0 <= cn < m or grid[rn][cn] == 1:
                    continue
                grid[rn][cn] = 1
                queue.append((rn, cn, dist + 1))
        return dist

    n = len(grid)
    queue = collections.deque([])
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                queue.append((i, j, 0))
    return bfs(queue) if len(queue) != n * n else -1

# dp, TC:O(N^2), SC:O(N^2)
def maxDistance2(grid: List[List[int]]) -> int:

    n = len(grid)
    dp = [[0] * n for _ in range(n)]
    land_cell = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                dp[i][j] = 1
                land_cell += 1
                continue
            dp[i][j] = min(dp[i][j - 1] if j > 0 else float('inf'),
                           dp[i - 1][j] if i > 0 else float('inf')) + 1  # left and top

    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            dist = min(dp[i][j + 1] if j < n - 1 else float('inf'),
                       dp[i + 1][j] if i < n - 1 else float('inf')) + 1  # right and down
            dp[i][j] = min(dp[i][j], dist)
    res = max(c for row in dp for c in row) - 1

    return -1 if land_cell == 0 or land_cell == n * n else res

# dp and store in-place, TC:O(N^2), SC:O(1)
def maxDistance2(grid: List[List[int]]) -> int:

    n = len(grid)
    land_cell = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                land_cell += 1
                continue
            grid[i][j] = min(grid[i][j - 1] if j > 0 else float('inf'),
                             grid[i - 1][j] if i > 0 else float('inf')) + 1  # left and top

    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            dist = min(grid[i][j + 1] if j < n - 1 else float('inf'),
                       grid[i + 1][j] if i < n - 1 else float('inf')) + 1  # right and down
            grid[i][j] = min(grid[i][j], dist)
    res = max(c for row in grid for c in row) - 1

    return -1 if land_cell == 0 or land_cell == n * n else res