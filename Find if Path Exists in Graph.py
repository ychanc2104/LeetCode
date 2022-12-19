# https://leetcode.com/problems/find-if-path-exists-in-graph/description/

import collections


# dfs, TC:O(N+M), SC:O(N+M)
def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    graph = collections.defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * n

    def dfs(node):
        if node == destination:
            return True
        if visited[node]:
            return False
        visited[node] = True
        for nei in graph[node]:
            if dfs(nei):
                return True
        return False

    return dfs(source)