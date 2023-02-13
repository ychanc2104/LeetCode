# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

import collections, math

# first thought, BFS, topsort, TC:O(N), SC:O(N)
def minimumFuelCost(roads: List[List[int]], seats: int) -> int:
    #
    n = len(roads) + 1
    counter = [1] * n
    graph = collections.defaultdict(set)
    for a, b in roads:
        graph[a].add(b)
        graph[b].add(a)

    queue = collections.deque([i for i in range(1, n) if len(graph[i]) == 1])  # node
    res = 0
    while queue:
        node = queue.popleft()
        for nei in graph[node]:
            res += math.ceil(counter[node] / seats)
            counter[nei] += counter[node]  # move to nei
            graph[nei].remove(node)
            if len(graph[nei]) == 1 and nei != 0:
                queue.append(nei)
    return res


# DFS, TC:O(N), SC:O(N)
def minimumFuelCost2(roads: List[List[int]], seats: int) -> int:
    #
    n = len(roads) + 1
    counter = [1] * n
    graph = collections.defaultdict(list)
    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a)
    res = 0
    def dfs(node, parent=-1):
        nonlocal res

        for nei in graph[node]:
            if nei != parent:
                counter[node] += dfs(nei, node) # count subtree people
        if node != 0:
            res += math.ceil(counter[node]/seats) # add fuel along path
        return counter[node]

    dfs(0)
        return res