# https://leetcode.com/problems/min-cost-to-connect-all-points/


# minimum spanning tree, Kruskal's algorithm, TC:O(N^2logN), SC:O(N^2)
def minCostConnectPoints(points: List[List[int]]) -> int:
    edges = [] # SC:O(N^2)
    n = len(points)
    for i in range(n): # TC:O(N^2)
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            edges.append((i, j, dist))
    if not edges: return 0
    # print(edges)
    edges.sort(key=lambda x: x[2]) # TC:O(2N^2logN)

    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px == py: return False
        parents[px] = py
        return True

    parents = [i for i in range(n)]
    res = 0
    count = n
    for x, y, dist in edges: # TC:O(N*alpha(N))
        if union(x, y):
            res += dist
            count -= 1
        if count == 1: return res
