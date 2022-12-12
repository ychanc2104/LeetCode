# https://leetcode.com/problems/the-maze/
# https://leetcode.com/problems/the-maze/solutions/150523/python-elegant-dfs-solution/

import collections

# dfs, TC:O(mn(m+n)) in worst, SC:O(mn)
def hasPath(maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
    n, m = len(maze), len(maze[0])
    visited = [[False] * m for _ in range(n)]
    dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))

    # dfs, only call dfs when hit the wall
    def dfs(r, c):
        if visited[r][c]: return False
        if [r, c] == destination: return True
        visited[r][c] = True  # mark visited of each start position
        for ro, co in dirs:
            rn, cn = r + ro, c + co
            while 0 <= rn < n and 0 <= cn < m and maze[rn][cn] == 0:  # rolling to the wall
                rn += ro
                cn += co
            if dfs(rn - ro, cn - co):  # start from corner again
                return True
        return False

    return dfs(*start)


# bfs, TC:O(mn(m+n)) in worst, SC:O(mn)
def hasPath2(maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
    n, m = len(maze), len(maze[0])
    visited = [[False]*m for _ in range(n)]
    dirs = ((1,0),(0,1),(-1,0),(0,-1))
    # bfs
    queue = collections.deque([start])
    while queue:
        r, c = queue.popleft()
        if visited[r][c]: continue
        visited[r][c] = True
        if [r,c] == destination: return True
        for ro,co in dirs: # four directions
            rn, cn = r+ro, c+co
            # go to the end
            while 0<=rn<n and 0<=cn<m and maze[rn][cn]==0:
                rn += ro
                cn += co
            queue.append((rn-ro, cn-co)) # start from corner
    return False