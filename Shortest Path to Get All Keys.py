# https://leetcode.com/problems/shortest-path-to-get-all-keys/
# https://leetcode.com/problems/shortest-path-to-get-all-keys/solutions/364604/python-level-by-level-bfs-solution-292-ms-beat-97-78-similar-problems-listed/

import collections

# bfs with multiple states, TC:O(V+E) = O(NM2^k+4k), SC:O(NMk+NM2^k) for visited + queue
def shortestPathAllKeys(grid: List[str]) -> int:
    # key status [0]*6 (k keys)
    n, m = len(grid), len(grid[0])
    k = 0
    for i in range(n):
        for j in range(m):
            cell = grid[i][j]
            if cell == '@':
                start = (i, j)
            elif cell.islower():
                k += 1

    step = 0
    queue = collections.deque([(start, [0] * 6, step)])
    visited = set()  # visited,key_status
    visited.add((start, tuple([0] * 6)))
    while queue: # O(V+E) = O(NM2^k + 4k) all visited states
        (r, c), status, step = queue.popleft()
        # print(r,c,status,step,queue)
        if sum(status) == k: return step
        for ro, co in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            rn, cn = r + ro, c + co
            if rn < 0 or cn < 0 or rn >= n or cn >= m or grid[rn][cn] == '#':
                continue
            if ((rn, cn), tuple(status)) in visited:
                continue
            visited.add(((rn, cn), tuple(status)))
            cell = grid[rn][cn]
            new_status = status.copy()  # original
            if cell.islower():  # key
                new_status[ord(cell) - ord('a')] = 1
                queue.append(((rn, cn), new_status, step + 1))
            elif cell.isupper():  # lock
                if status[ord(cell.lower()) - ord('a')]:  # with its key
                    queue.append(((rn, cn), new_status, step + 1))
            elif cell in '.@':  # go
                queue.append(((rn, cn), new_status, step + 1))
    return -1