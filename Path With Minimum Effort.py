# https://leetcode.com/problems/path-with-minimum-effort/
# https://leetcode.com/problems/path-with-minimum-effort/solutions/909017/java-python-dijikstra-binary-search-clean-concise/

import heapq, collections

# binary search + dfs, TC:O(NMlogk) k is 10^6 here, SC:O(NM)
def minimumEffortPath(heights: List[List[int]]) -> int:
    n, m = len(heights), len(heights[0])

    # binary search of each answer
    def check(k):  # TC:O(NM), SC:O(NM)
        stack = [(0, 0)]  # r,c,effort
        visited = [[False] * m for _ in range(n)]
        while stack:
            r, c = stack.pop()
            if r == n - 1 and c == m - 1: return True
            h = heights[r][c]
            visited[r][c] = True
            for ro, co in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                rn, cn = r + ro, c + co
                if rn < 0 or cn < 0 or rn >= n or cn >= m or visited[rn][cn] or abs(h - heights[rn][cn]) > k:
                    continue
                stack.append((rn, cn))
        return False

    L, R = 0, 10 ** 6
    while L <= R:  # TC:O(NMlogk)
        mid = (L + R) // 2
        if check(mid):  # try smaller
            R = mid - 1
        else:
            L = mid + 1
    return L


# minimum spanning tree, Kruskal's algorithm(union find), TC:O(NM*alpha(NM) + NMlogNM), SC:O(NM)
def minimumEffortPath2(heights: List[List[int]]) -> int:
    # union find
    n, m = len(heights), len(heights[0])
    edges = []
    for r in range(n): # TC:O(NM), SC:O(NM)
        for c in range(m):
            for ro,co in ((1,0),(0,1)): # directed or ((1,0),(0,1),(-1,0),(0,-1))
                rn, cn = r+ro, c+co
                if rn < 0 or cn < 0 or rn >= n or cn >= m:
                    continue
                diff = abs(heights[r][c] - heights[rn][cn])
                edges.append((c+r*m, cn+rn*m, diff)) # from, to, diff
    if not edges: return 0
    edges.sort(key=lambda x: x[2]) # TC:O(NMlogNM), SC:O(NM)
    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]
    def union(x, y):
        px, py = find(x), find(y)
        parents[px] = py
    parents = [i for i in range(n*m)]
    # do union until find(0) == find(n*m-1)
    for a, b, diff in edges: # TC:O(NM*alpha(NM))
        union(a, b)
        if find(0) == find(n*m-1):
            return diff


# Dijkstra(TLE)
def minimumEffortPath3(heights: List[List[int]]) -> int:
    n, m = len(heights), len(heights[0])
    # use heaps, go path with min effort
    heaps = [(0,0,0)] # effort,r,c,visited
    visited = [[False]*m for _ in range(n)]
    while heaps:
        effort, r, c = heapq.heappop(heaps) # big row and col first
        if r == n-1 and c == m-1: return effort
        visited[r][c] = True
        # explore
        for ro, co in ((1,0),(0,1),(-1,0),(0,-1)):
            rn, cn = r+ro, c+co
            if rn < 0 or cn < 0 or rn >= n or cn >= m or visited[rn][cn]: continue
            e2 = abs(heights[r][c] - heights[rn][cn])
            heapq.heappush(heaps, (max(e2, effort), rn, cn))


# modified Dijkstra(dp), TC:O(NMlogNM), SC:O(NM)
def minimumEffortPath4(heights: List[List[int]]) -> int:
    n, m = len(heights), len(heights[0])
    # use heaps, go path with min effort
    heaps = [(0,0,0)] # effort,r,c,visited
    visited = [[False]*m for _ in range(n)]
    dp = [[float("inf")]*m for _ in range(n)] # dp[i][j]: min of max effort from (0,0) to (i,j)
    dp[0][0] = 0
    while heaps:
        effort, r, c = heapq.heappop(heaps) # big row and col first
        if effort > dp[r][c]: continue # skip old
        # if r == n-1 and c == m-1: return effort
        visited[r][c] = True
        # explore
        for ro, co in ((1,0),(0,1),(-1,0),(0,-1)):
            rn, cn = r+ro, c+co
            if rn < 0 or cn < 0 or rn >= n or cn >= m or visited[rn][cn]: continue
            e2 = max(effort, abs(heights[r][c] - heights[rn][cn])) # choose bigger effort
            if dp[rn][cn] > e2:
                dp[rn][cn] = e2 # update min effort
                heapq.heappush(heaps, (e2, rn, cn))
    return dp[-1][-1]


# Minimum Spanning Tree, heaps(Prim's algorithm), TC:O(NMlogNM), SC:O(NM)
def minimumEffortPath4(heights: List[List[int]]) -> int:
    n, m = len(heights), len(heights[0])
    graph = collections.defaultdict(list)
    for r in range(n): # TC:O(NM), SC:O(NM)
        for c in range(m):
            for ro,co in ((1,0),(0,1)): # directed or ((1,0),(0,1),(-1,0),(0,-1))
                rn, cn = r+ro, c+co
                if rn < 0 or cn < 0 or rn >= n or cn >= m:
                    continue
                diff = abs(heights[r][c] - heights[rn][cn])
                x, y = c + r*m, cn + rn*m
                graph[x].append((rn, cn, diff))
                graph[y].append((r, c, diff))
    # heaps
    heaps = [(0,0,0)] # r,c,diff
    visited = [False for _ in range(n*m)]
    res = 0
    while heaps:
        # print(heaps)
        effort, r, c = heapq.heappop(heaps)
        if r==n-1 and c==m-1: return effort # min effort
        idx = c + r*m
        visited[idx] = True
        for rn, cn, diff in graph[idx]:
            if visited[cn + rn*m]: continue
            heapq.heappush(heaps, (max(effort, diff), rn, cn))