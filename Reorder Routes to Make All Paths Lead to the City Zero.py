# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/solutions/661774/python3-easy-short-dfs/

import collections


# dfs, TC:O(N+M), SC:O(M)
def minReorder(n: int, connections: List[List[int]]) -> int:
    res = 0
    graph = collections.defaultdict(list)
    directions = set()
    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)
        directions.add((a, b))

    def dfs(node=0, parent=-1):
        nonlocal res

        if (parent, node) in directions:
            res += 1
        for nei in graph[node]:
            if nei == parent: continue
            dfs(nei, node)

    dfs(0, -1)

    return res