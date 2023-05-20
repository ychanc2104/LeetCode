# https://leetcode.com/problems/walls-and-gates/description/

import collections

# BFS, TC:O(NM), SC:O(NM)
def wallsAndGates(rooms: List[List[int]]) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    """
    queue = collections.deque([])
    m, n = len(rooms), len(rooms[0])
    for i in range(m):
        for j in range(n):
            if rooms[i][j] == 0:
                queue.append((i, j, 0))
    inf = 2 ** 31 - 1
    while queue:
        r, c, s = queue.popleft()
        for rn, cn in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)):
            if not 0 <= rn < m or not 0 <= cn < n or rooms[rn][cn] != inf:
                continue
            rooms[rn][cn] = s + 1
            queue.append((rn, cn, s + 1))