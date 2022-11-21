# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/

import collections

# BFS, TC:O(NM), SC:O(max(N,M)) pi*D, Diameter ~= sqrt(N^2 + M^2) worst in max(N,M)
def nearestExit(maze: List[List[str]], entrance: List[int]) -> int:
    # do BFS, go for '.'
    n, m = len(maze), len(maze[0])
    queue = collections.deque([(entrance, 0)])
    maze[entrance[0]][entrance[1]] = '+'
    while queue:
        (r, c), step = queue.popleft()
        if step and (r == 0 or r == n - 1 or c == 0 or c == m - 1):
            return step
        # explore four directions
        for ro, co in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            r2, c2 = r + ro, c + co
            if r2 < 0 or c2 < 0 or r2 >= n or c2 >= m or maze[r2][c2] == '+': continue
            queue.append([(r2, c2), step + 1])
            maze[r2][c2] = '+'  # mark visited
    return -1