# https://leetcode.com/problems/swim-in-rising-water/

import heapq

# minimum spanning tree, Kruskal's algorithm(union find), TC:O(N^2*logN), SC:O(N^2)
def swimInWater(grid: List[List[int]]) -> int:
    # sort all grid according to their weight
    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        px, py = find(x), find(y)
        parents[px] = parents[py]

    # build all edges
    edges = []
    n = len(grid)
    for i in range(n):
        for j in range(n):
            edges.append((i, j, grid[i][j]))
    # sort by weight
    edges.sort(key=lambda x: x[2]) # TC:O(N^2logN)
    parents = [i for i in range(n * n)]
    dest = parents[-1]
    # union each edge with its neighbor until start and end are the same parent
    for i, j, w in edges: # TC:O(N^2*alpha(N^2))
        for ro, co in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            rn, cn = i + ro, j + co
            if rn < 0 or cn < 0 or rn >= n or cn >= n or grid[rn][cn] > grid[i][j]: continue
            union(j + i * n, cn + rn * n)  # union with neighbor
        if find(0) == find(dest):
            return w

# heaps, TC:O(N^2*logN), SC:O(N^2)
def swimInWater2(grid: List[List[int]]) -> int:
    n = len(grid)
    res = grid[0][0]
    heaps = [(res, 0, 0)]
    visited = set([(0,0)])
    while heaps:
        height, r, c = heapq.heappop(heaps)
        res = max(res, height)
        if r==n-1 and c==n-1: return res # reach
        for ro, co in ((1,0),(0,1),(-1,0),(0,-1)): # do not add visited node into heaps
            rn, cn = r+ro, c+co
            if rn < 0 or cn < 0 or rn >= n or cn >= n or (rn,cn) in visited: continue
            visited.add((rn, cn))
            heapq.heappush(heaps, (grid[rn][cn], rn, cn))
    return res


# binary search, TC:O(N^2*logN), SC:O(N^2)
def swimInWater3(grid: List[List[int]]) -> int:
    n = len(grid)

    def check(T):  # TC:O(N^2)
        # go from (0,0)
        stack = [(0, 0)]
        visited = set(stack)
        while stack:
            r, c = stack.pop()
            if r == n - 1 and c == n - 1: return True
            for ro, co in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                rn, cn = r + ro, c + co
                if rn < 0 or cn < 0 or rn >= n or cn >= n or (rn, cn) in visited or grid[rn][cn] > T:
                    continue
                visited.add((rn, cn))
                stack.append((rn, cn))
        return False

    L, R = grid[0][0], max(x for row in grid for x in row)  # TC:O(N^2) or use n**2 (upper bound)
    while L <= R:
        mid = (L + R) // 2
        if check(mid):  # can reach, try smaller T
            R = mid - 1
        else:
            L = mid + 1
    return L
