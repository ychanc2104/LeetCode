# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/
# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/solutions/524828/python-o-mn-simple-bfs-with-explanation/


import heapq, collections

# first thought(TLE) heaps, TC:O(NMlogNM), SC:O(NM)
def minCost(grid: list[list[int]]) -> int:
    n, m = len(grid), len(grid[0])
    heaps = [(0, 0, 0)]  # cost, r, c
    visited = [[False] * m for _ in range(n)]
    while heaps:
        cost, r, c = heapq.heappop(heaps)
        if r == n - 1 and c == m - 1: return cost
        cell = grid[r][c]
        visited[r][c] = True
        # explore
        for ro, co in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            rn, cn = r + ro, c + co
            if rn < 0 or cn < 0 or rn >= n or cn >= m or visited[rn][cn]: continue
            if (cell == 1 and co == 1) or (cell == 2 and co == -1) or (cell == 3 and ro == 1) or (
                    cell == 4 and ro == -1):
                heapq.heappush(heaps, (cost, rn, cn))  # no need to increase cost
            else:
                heapq.heappush(heaps, (cost + 1, rn, cn))

# dp+BFS+greedy, TC:O(NM), SC:O(NM)
def minCost2(grid: list[list[int]]) -> int:
    arrow = ((0, 1), (0, -1), (1, 0), (-1, 0))
    n, m = len(grid), len(grid[0])
    queue = collections.deque([(0, 0, 0)])  # cost, r, c
    dp = {}  # (r,c):cost

    while queue:
        cost, r, c = queue.popleft()
        while 0 <= r < n and 0 <= c < m and (r, c) not in dp:  # in bound and no duplicate
            if r == n - 1 and c == m - 1: return cost # first meet end must be the answer
            dp[(r, c)] = cost  # mark visit and no adding cost
            # four directions add to queue, arrow direction will eliminate by (r,c) in dp
            for ro, co in arrow: # no need to concern about the cost of arrow direction will become cost+1
                queue.append((cost + 1, r + ro, c + co))
            ro, co = arrow[grid[r][c] - 1]
            r, c = r + ro, c + co  # move along arrow direction until out of bound
    # return dp[(n - 1, m - 1)] # or use this


# dp+BFS+greedy, TC:O(NM), SC:O(NM)
def minCost3(grid: list[list[int]]) -> int:
    arrow = ((0,1),(0,-1),(1,0),(-1,0))
    n, m = len(grid), len(grid[0])
    queue = collections.deque([(0,0,0)]) # cost, r, c
    visited = [[False]*m for _ in range(n)]
    while queue:
        cost, r, c = queue.popleft()
        while 0<=r<n and 0<=c<m and not visited[r][c]: # in bound and no duplicate
            if r==n-1 and c==m-1: return cost # first meet end must be the answer
            visited[r][c] = True # mark visit
            # four directions add to queue, arrow direction will eliminate by (r,c) in dp
            for ro,co in arrow: # no need to concern about the cost of arrow direction will become cost+1
                queue.append((cost+1, r+ro, c+co))
            ro, co = arrow[grid[r][c]-1]
            r, c = r+ro, c+co # move along arrow direction until out of bound



grid = [[2,1,2,4,4,3,4,3,3,1,2,3,3,2,4,3,2,2,4,4,2,3,1,2,2,3,2,4,4,4,4,4,2,4,2,4,3,4,1,2,4,1,1,1,3,2,3,2,4],[3,3,1,4,3,1,3,1,4,1,2,4,1,1,2,4,2,4,2,3,1,2,2,4,4,1,2,4,1,1,2,1,4,3,2,3,1,3,1,3,2,2,1,3,1,2,4,3,4],[3,2,3,4,3,4,3,3,1,1,1,3,1,3,4,2,1,4,2,2,3,1,4,4,4,1,3,1,2,3,3,1,1,1,4,1,3,2,1,4,3,4,4,1,4,2,4,4,3],[3,3,3,2,2,3,2,4,3,4,4,1,4,2,3,4,3,1,2,3,2,4,1,4,2,4,4,3,2,4,1,3,1,1,3,3,4,3,3,2,3,2,1,1,2,3,2,2,1],[4,3,3,1,1,1,3,1,4,2,4,2,3,4,4,2,1,4,3,2,3,3,3,2,1,2,4,4,2,1,1,4,4,4,1,2,3,1,1,3,3,3,1,4,1,4,3,4,2],[3,4,4,2,4,3,4,3,3,4,1,4,2,4,1,1,1,1,1,3,3,1,3,1,2,3,3,1,4,4,3,1,3,2,2,1,1,4,4,2,1,1,4,2,3,1,2,4,2],[2,4,1,2,4,3,3,4,4,1,2,3,3,2,4,1,1,2,4,3,1,3,2,2,2,3,3,3,1,4,2,3,1,2,4,1,4,1,2,4,4,2,4,3,4,2,3,4,4],[4,2,2,1,3,1,4,1,2,3,4,3,1,1,1,3,3,4,4,1,4,1,4,2,4,4,1,4,3,2,2,3,1,1,4,3,2,4,2,4,1,3,3,4,2,4,4,1,4],[3,1,3,3,4,1,2,4,4,1,1,3,4,4,4,1,2,1,3,1,1,2,2,3,3,2,2,2,2,2,1,4,2,4,4,1,4,2,4,4,1,3,3,4,4,2,4,2,1],[4,1,1,2,4,3,2,2,4,4,3,4,3,2,2,1,3,3,4,4,3,3,3,2,3,3,3,3,4,2,4,2,2,4,4,2,4,4,3,1,4,1,4,1,2,2,4,1,4],[4,2,2,2,1,4,2,1,1,2,1,4,1,3,3,3,2,3,4,1,3,1,3,4,2,1,4,1,3,2,4,2,2,2,4,1,2,3,3,3,1,4,3,1,3,4,3,4,4],[2,1,2,1,2,4,1,2,2,3,4,2,3,3,2,2,3,2,4,4,1,1,3,2,4,1,4,2,3,1,3,4,4,3,1,3,1,4,2,2,1,1,4,3,1,2,2,3,1],[4,1,3,4,4,2,1,4,2,2,2,3,4,4,4,3,2,3,2,2,3,4,4,2,4,2,4,4,4,2,3,4,1,2,3,3,3,1,3,1,3,3,4,3,3,1,1,3,4],[1,1,4,2,2,3,4,4,4,2,4,3,4,1,2,2,2,3,1,2,3,2,3,1,4,1,4,4,4,1,2,2,3,2,4,4,2,4,4,2,1,3,2,4,2,1,4,4,1],[4,2,2,3,2,1,4,4,2,2,3,1,4,2,1,2,2,1,1,4,4,3,1,4,3,3,1,3,4,1,3,2,4,1,3,3,3,1,4,3,2,1,2,4,2,1,4,1,3],[2,1,2,4,4,4,3,2,4,4,3,2,2,2,3,1,4,3,2,4,3,4,2,2,1,2,1,2,3,3,2,4,2,4,3,3,4,2,4,4,1,4,4,3,2,3,4,1,1],[1,2,2,1,1,3,4,4,2,2,1,4,2,3,2,2,1,4,3,3,2,3,3,3,3,4,1,3,2,1,4,2,2,1,1,3,3,1,2,1,4,3,1,1,4,4,4,3,2],[4,2,3,3,1,1,3,2,2,1,1,2,4,2,2,1,1,1,2,3,4,4,3,3,1,1,2,4,1,3,1,4,3,2,3,3,1,2,4,3,1,3,1,2,3,4,2,1,2],[1,4,2,4,4,1,1,1,1,3,4,3,4,1,2,3,1,1,2,3,4,3,4,3,1,2,4,2,4,1,2,3,2,4,4,2,2,4,2,3,2,2,1,4,3,4,3,4,3],[3,2,3,4,4,1,2,3,2,2,3,1,4,1,2,3,4,4,4,3,2,1,3,1,3,4,3,4,2,3,1,4,4,4,4,4,3,3,2,3,2,1,2,4,4,2,4,1,1],[1,1,1,4,3,2,3,1,4,2,2,4,3,2,3,2,1,1,2,2,3,2,1,3,4,1,2,4,1,2,3,1,2,1,3,1,3,1,1,3,1,3,3,4,4,3,2,4,1],[3,3,4,4,4,2,1,2,3,4,2,4,2,2,2,4,4,2,1,2,4,4,2,1,4,4,1,1,2,2,4,2,2,2,1,1,1,2,4,2,2,2,3,3,2,1,2,3,2],[1,3,4,4,4,2,2,3,2,4,2,4,2,3,1,3,3,4,2,2,2,1,4,4,1,4,1,4,3,3,2,4,4,1,1,4,4,3,4,3,1,2,2,2,4,4,3,2,3],[3,2,3,1,1,1,4,4,4,1,3,4,4,3,1,1,4,4,3,4,1,4,4,1,4,2,3,4,3,2,2,1,2,4,4,3,4,1,2,1,2,3,2,2,2,2,3,2,1],[2,4,2,1,3,2,2,3,2,1,2,4,2,1,1,2,1,2,3,4,4,4,3,1,3,2,1,1,3,3,3,2,3,4,3,2,3,1,1,2,4,4,3,1,4,4,1,3,2],[1,4,3,3,3,3,3,3,2,3,3,2,2,2,4,2,3,3,4,2,4,2,2,4,4,1,1,4,1,1,2,1,4,4,4,2,4,2,3,4,3,2,2,4,4,1,2,3,1],[1,4,2,3,2,1,4,3,2,2,2,4,4,2,3,3,1,4,1,2,3,1,3,4,3,1,3,4,1,1,3,3,4,2,4,3,3,3,1,4,1,1,4,2,1,2,3,4,1],[2,1,1,1,1,4,1,1,4,2,1,1,1,3,3,4,1,3,1,4,3,1,2,4,1,2,2,4,1,1,1,2,1,4,2,2,3,3,1,3,2,4,3,4,4,3,1,2,4],[4,1,3,1,4,4,3,1,1,1,2,1,4,2,3,4,3,2,2,4,4,3,3,1,2,4,4,2,1,2,1,1,3,1,4,1,1,1,2,1,2,4,2,3,4,3,1,1,2],[2,1,4,2,2,4,4,1,2,1,2,4,4,3,3,4,4,2,3,1,3,3,2,3,3,4,3,4,4,4,4,1,4,4,3,1,1,1,1,1,2,1,4,2,1,1,2,3,3],[3,2,4,3,4,4,1,1,3,2,4,3,1,1,3,2,1,1,4,2,3,2,3,1,3,4,1,4,4,2,3,2,4,1,2,2,2,4,4,4,2,3,3,3,2,4,4,2,2],[4,3,2,1,3,3,1,3,3,3,4,3,4,1,3,3,2,2,2,3,3,3,1,1,1,2,3,2,2,3,3,2,2,2,2,3,2,4,1,3,1,2,4,2,4,3,1,1,4],[4,3,4,2,3,1,4,1,2,3,1,4,4,1,4,2,3,3,1,1,1,3,4,2,1,3,1,3,2,3,4,4,1,3,3,4,3,1,4,1,4,2,2,4,2,4,3,4,2],[2,3,2,3,2,2,1,4,3,3,2,4,4,3,2,3,1,1,3,2,2,3,2,3,1,3,2,1,1,3,1,1,1,3,3,3,4,1,2,2,4,2,3,2,3,3,3,2,1],[2,3,1,3,3,2,4,2,1,3,4,3,3,1,1,1,1,2,3,1,2,3,4,2,4,3,4,2,1,2,3,3,2,3,1,4,4,1,3,2,2,4,2,3,1,3,4,3,3],[4,2,2,4,3,1,4,3,1,2,3,2,2,1,2,2,1,4,2,2,3,2,2,2,1,1,2,3,4,3,4,3,4,3,1,1,2,2,2,4,1,3,1,3,1,1,2,4,2],[1,1,3,4,2,4,4,2,2,1,2,1,4,1,3,3,3,4,1,3,2,1,3,2,4,3,3,1,3,3,3,1,3,4,2,1,1,3,4,2,2,1,2,3,2,2,1,2,1]]
res = minCost(grid)