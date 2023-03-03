# https://leetcode.com/problems/path-with-maximum-minimum-value/description/


import heapq

# bfs + heaps + dp (Dijkstra), TC:O(NMlogNM), SC:O(NM)
def maximumMinimumPath(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dp = [[-1] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    heaps = [(-grid[0][0], 0, 0)]  # -score, r, c

    while heaps:
        score, r, c = heapq.heappop(heaps)
        if r == m - 1 and c == n - 1:
            return -score
        for rn, cn in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)):
            if not 0 <= rn < m or not 0 <= cn < n:
                continue
            if min(-score, grid[rn][cn]) > dp[rn][cn]:
                dp[rn][cn] = min(-score, grid[rn][cn])
                heapq.heappush(heaps, (-min(-score, grid[rn][cn]), rn, cn))


# MST, Kruskal's algorithm(union find), TC:O(NMlogNM), SC:O(NM)
def maximumMinimumPath2(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    vertices = []
    parents = [i for i in range(n * m)]
    rank = [0 for _ in range(n * m)]
    for i in range(m):
        for j in range(n):
            vertices.append((grid[i][j], i, j))
    vertices.sort(reverse=True)

    # print(parents)
    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y): # union by rank
        px, py = find(x), find(y)
        if rank[px] < rank[py]:
            parents[px] = py
        elif rank[px] > rank[py]:
            parents[py] = px
        else:
            parents[px] = py
            rank[py] += 1

    for w, r, c in vertices:
        for rn, cn in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)):
            if not 0 <= rn < m or not 0 <= cn < n or grid[rn][cn] < grid[r][c]: continue
            union(c + r * n, cn + rn * n)
        if find(0) == find(n * m - 1):
            return w


# binary search + dfs, TC:O(NMlogNM), SC:O(NM)
def maximumMinimumPath3(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    def reachable(val): # TC:O(NM), SC:O(NM)
        visited = set()
        def dfs(r, c):
            if grid[r][c] < val:
                return False
            if r==m-1 and c==n-1:
                return True
            for rn, cn in ((r+1,c),(r,c+1),(r-1,c),(r,c-1)):
                if not 0<=rn<m or not 0<=cn<n or (rn,cn) in visited:
                    continue
                visited.add((rn, cn))
                if dfs(rn, cn):
                    return True
            return False
        return dfs(0, 0)

    L, R = 0, 10**9
    while L <= R:
        mid = (L+R)//2
        if reachable(mid): # can reach end, increase value
            L = mid + 1
        else:
            R = mid - 1
    return R