# https://leetcode.com/problems/the-maze-ii/

import heapq

# Dijkstra + dp, TC:O(NMlogNM), SC:O(NM)
def shortestDistance(maze: List[List[int]], start: List[int], destination: List[int]) -> int:
    n, m = len(maze), len(maze[0])
    heaps = [(0, start)]
    # TC:O(NM), SC:O(NM)
    dp = [[float('inf')] * m for _ in range(n)]  # dp[i][j]: min step from start to (i,j)
    dp[start[0]][start[1]] = 0
    while heaps:  # TC:O(NMlogNM), SC:O(NM)
        step, (r, c) = heapq.heappop(heaps)  # min step first
        if [r, c] == destination:  # min path
            return step
        for ro, co in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            rn, cn = r + ro, c + co
            temp_step = step
            while 0 <= rn < n and 0 <= cn < m and maze[rn][cn] == 0:
                rn += ro
                cn += co
                temp_step += 1
            if temp_step < dp[rn - ro][cn - co]:  # only when become smaller step
                dp[rn - ro][cn - co] = temp_step
                heapq.heappush(heaps, (temp_step, (rn - ro, cn - co)))
    return -1
