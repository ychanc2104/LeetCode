# https://leetcode.com/problems/optimize-water-distribution-in-a-village/


# minimum spanning tree + trick(add 0 node into pipes), Kruskal's algorithm, TC:O((N+M)log(N+M)) M is len of pipes, SC:O(N+M)
def minCostToSupplyWater(n: int, wells: List[int], pipes: List[List[int]]) -> int:
    # add 0 node as well cost
    for i, cost in enumerate(wells, 1): # TC:O(N)
        pipes.append((0, i, cost))
    # sort pipes
    pipes.sort(key=lambda x: x[2]) # TC:O((N+M)log(N+M)), SC:O(N+M)

    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px == py: return False
        parents[px] = py
        return True

    parents = [i for i in range(n + 1)] # SC:O(N)
    res = 0
    count = n + 1
    for i, j, cost in pipes:
        if union(i, j):
            res += cost
            count -= 1
        if count == 1:
            return res