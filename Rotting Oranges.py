# https://leetcode.com/problems/rotting-oranges/

import collections

# first thought, BFS, TC:O(N*M), SC:O(N*M), worst case for all rotting oranges
def orangesRotting(grid) -> int:
    queue = collections.deque([])
    # find rotting oranges
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j))
    # start rotting oranges
    res = 0
    while queue:
        neighbors = []
        for i, j in queue:
            # append all neighbors
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                r, c = i + y, j + x
                if not (r < 0 or c < 0 or r >= m or c >= n) and grid[r][c] == 1:
                    neighbors.append((r, c))
                    grid[r][c] = 2
        res += 1 if neighbors else 0
        queue = neighbors
    # final check if oranges are not rotting
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                return -1
    return res



# add n_fresh to save final loop
def orangesRotting2(grid) -> int:    # bfs
    queue = collections.deque([])
    n_fresh = 0
    # find rotting oranges
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                n_fresh += 1
            if grid[i][j] == 2:
                queue.append((i, j))
    # start rotting oranges
    res = 0
    while queue:
        neighbors = []
        for i, j in queue:
            # append all neighbors
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                r, c = i + y, j + x
                if not (r < 0 or c < 0 or r >= m or c >= n) and grid[r][c] == 1:
                    neighbors.append((r, c))
                    grid[r][c] = 2
                    n_fresh -= 1
        res += 1 if neighbors else 0
        queue = neighbors
    return res if n_fresh == 0 else -1

# clean solution
def orangesRotting3(grid) -> int:  # bfs
    row, col = len(grid), len(grid[0])
    rotting = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}
    fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}
    timer = 0
    while fresh:
        if not rotting: return -1
        rotting = {(i + di, j + dj) for i, j in rotting for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)] if
                   (i + di, j + dj) in fresh}
        fresh -= rotting
        timer += 1
    return timer
