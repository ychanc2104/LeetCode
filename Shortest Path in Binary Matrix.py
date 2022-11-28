# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

import collections

# BFS 8 directions, TC:O(N^2), SC:O(N^2)
def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    if grid[0][0] == 1: return -1
    queue = collections.deque([((0, 0), 1)])
    grid[0][0] = 1
    n = len(grid)
    while queue:
        (r, c), step = queue.popleft()
        if (r, c) == (n - 1, n - 1): return step
        for ro, co in ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)):
            rn, cn = r + ro, c + co
            if rn < 0 or cn < 0 or rn >= n or cn >= n or grid[rn][cn] == 1:
                continue
            grid[rn][cn] = 1
            queue.append(((rn, cn), step + 1))
    return -1