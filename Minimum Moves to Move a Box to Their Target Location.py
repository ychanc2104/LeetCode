# https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/description/
# https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/solutions/693918/python-bfs-bfs-130ms-beats-95-explained-commented/

import collections

# bfs twice, TC:O(N^2M^2), SC:O(N^2M^2)
def minPushBox(grid: List[List[str]]) -> int:
    # bfs from box, move dir only when its back is empty
    # check person can do bfs to the back of box
    n, m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m):
            cell = grid[i][j]
            if cell == 'S':
                player = (i, j)
            elif cell == 'B':
                box = (i, j)
            elif cell == 'T':
                dest = (i, j)

    def reachable(start, end, box): # TC:O(NM)
        queue = collections.deque([start])
        visited = [[False] * m for _ in range(n)]
        while queue:
            r, c = queue.popleft()
            if (r, c) == end:
                return True
            for ro, co in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                rn, cn = r + ro, c + co
                if rn < 0 or cn < 0 or rn >= n or cn >= m or visited[rn][cn] or grid[rn][cn] == '#' or (rn, cn) == box:
                    continue
                visited[rn][cn] = True
                queue.append((rn, cn))
        return False

    # bfs from the box and check person movement using bfs
    step = 0
    queue = collections.deque([(box, player, step)])
    visited = set() # SC:O(NM*NM), two comp
    while queue:
        box, player, step = queue.popleft()
        # print(box, player, step, dest)
        if box == dest: return step
        r, c = box
        for ro, co in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            rn, cn = r + ro, c + co  # desried to move
            rb, cb = r - ro, c - co  # player should be placed
            if rn < 0 or cn < 0 or rn >= n or cn >= m or ((rn, cn), (rb, cb)) in visited or grid[rn][cn] == '#':
                continue
            if rb < 0 or cb < 0 or rb >= n or cb >= m or grid[rb][cb] == '#' or not reachable(player, (rb, cb), box):
                continue
            visited.add(((rn, cn), (rb, cb))) # do not push to the same direction
            queue.append(((rn, cn), box, step + 1))
    return -1

