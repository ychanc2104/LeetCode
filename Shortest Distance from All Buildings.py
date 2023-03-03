# https://leetcode.com/problems/shortest-distance-from-all-buildings/
# https://leetcode.com/problems/shortest-distance-from-all-buildings/solutions/76877/python-solution-72ms-beats-100-bfs-with-pruning/

import collections

# first thought, bfs (TLE), TC:O(N^2M^2), SC:O(NM)
def shortestDistance(grid: List[List[int]]) -> int:
    buildings = []
    lands = []
    n, m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m):
            cell = grid[i][j]
            if cell == 1:
                buildings.append((i, j))
            elif cell == 0:
                lands.append((i, j))
    # do bfs of each lands
    buildings_set = set(buildings)
    res = float('inf')
    for i, j in lands:
        totalStep = 0
        queue = collections.deque([(i, j, 0)])
        visited = [[False] * m for _ in range(n)]
        n_visited = 0
        while queue:
            r, c, step = queue.popleft()
            for ro, co in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                rn, cn = r + ro, c + co
                if rn < 0 or cn < 0 or rn >= n or cn >= m or visited[rn][cn] or grid[rn][cn] == 2:
                    continue
                visited[rn][cn] = True
                if (rn, cn) in buildings_set:
                    totalStep += step + 1
                    n_visited += 1
                    continue
                queue.append((rn, cn, step + 1))
        res = min(res, totalStep) if n_visited == len(buildings_set) else res
    return res if res != float('inf') and res > 0 else -1

def shortestDistance2(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    total_sum = [[0] * cols for _ in range(rows)]

    def bfs(row, col, curr_count):
        min_distance = math.inf
        queue = deque()
        queue.append([row, col, 0])
        while queue:
            curr_row, curr_col, curr_step = queue.popleft()
            for d in dirs:
                next_row = curr_row + d[0]
                next_col = curr_col + d[1]
                if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == -curr_count:
                    total_sum[next_row][next_col] += curr_step + 1
                    min_distance = min(min_distance, total_sum[next_row][next_col])
                    grid[next_row][next_col] -= 1
                    queue.append([next_row, next_col, curr_step + 1])
        return min_distance

    count = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                min_distance = bfs(row, col, count)
                count += 1
                if min_distance == math.inf:
                    return -1

    return min_distance


# bfs and count from buildings, TC:O(N^2M^2), SC:O(NM)
def shortestDistance3(grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    dist = [[[0,0] for _ in range(m)] for _ in range(n)] # step, n visited buildings
    n_buildings = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 1: continue
            # do bfs from buildings
            n_buildings += 1
            queue = collections.deque([(i, j, 0)])
            visited = [[False] * m for _ in range(n)]
            while queue: # TC:O(V+E)
                r, c, step = queue.popleft()
                for ro, co in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    rn, cn = r + ro, c + co
                    if rn < 0 or cn < 0 or rn >= n or cn >= m or visited[rn][cn] or grid[rn][cn] != 0:
                        continue
                    visited[rn][cn] = True
                    dist[rn][cn][0] += step+1
                    dist[rn][cn][1] += 1
                    queue.append((rn, cn, step + 1))
    res = float('inf')
    for i in range(n):
        for j in range(m):
            if dist[i][j][1] == n_buildings:
                res = min(res, dist[i][j][0])
    return res if res != float('inf') else -1


# bfs and count from buildings, TC:O(N^2M^2), SC:O(NM)
def shortestDistance4(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    starts = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                starts.append((i, j))

    dists = [[0] * n for _ in range(m)]
    visited_all = None
    for r, c in starts:
        visited = set()
        queue = collections.deque([(r, c, 0)])
        while queue:
            r, c, step = queue.popleft()
            for rn, cn in ((r+1,c),(r,c+1),(r-1,c),(r,c-1)):
                if not 0<=rn<m or not 0<=cn<n or grid[rn][cn] in [1,2] or (rn,cn) in visited:
                    continue
                visited.add((rn, cn))
                dists[rn][cn] += step+1
                queue.append((rn, cn, step+1))
        if visited_all is None:
            visited_all = visited
        else:
            visited_all &= visited
        # print(visited_all)
    res = float('inf')
    for i in range(m):
        for j in range(n):
            if dists[i][j] == 0 or (i,j) not in visited_all: continue
            res = min(res, dists[i][j])
    return res if res != float('inf') else -1