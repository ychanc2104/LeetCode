# https://leetcode.com/problems/connecting-cities-with-minimum-cost/
# https://leetcode.com/problems/connecting-cities-with-minimum-cost/solutions/369727/python-prim-kruskal/

import collections, heapq

# Minimum Spanning Tree, union find (Kruskal's algorithm), TC:O(M*alpha(N) + MlogM) M is len of connections, SC:O(N)
def minimumCost(n: int, connections: List[List[int]]) -> int:
    # do union find and sort by lowest cost first
    connections.sort(key=lambda x: x[2])

    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px == py:  # do nothing
            return False
        parents[px] = py
        return True

    parents = [i for i in range(n)]
    count = n
    res = 0
    for x, y, cost in connections:
        if union(x - 1, y - 1):
            res += cost
            count -= 1
    return res if count == 1 else -1

# Minimum Spanning Tree, heaps(Prim's algorithm), TC:O(M + MlogM) M is len of connections, SC:O(M)
def minimumCost2(n: int, connections: List[List[int]]) -> int:
    graph = collections.defaultdict(list)
    for x, y, cost in connections: # TC:O(M), SC:O(M)
        graph[x].append((y, cost))
        graph[y].append((x, cost))

    heaps = [(0, 1)]  # start from 1 (cost,city)
    visited = set()
    res = 0
    # BFS
    while heaps: # TC:O(MlogM)
        cost, city = heapq.heappop(heaps)
        if city in visited: continue
        visited.add(city)
        res += cost
        for nei, c in graph[city]:
            if nei in visited: continue  # do not go back
            heapq.heappush(heaps, (c, nei))
    return res if len(visited) == n else -1