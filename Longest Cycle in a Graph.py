# https://leetcode.com/problems/longest-cycle-in-a-graph/description/

import collections

# first thought, dfs, TC:O(N), SC:O(N)
def longestCycle(edges: List[int]) -> int:
    visited = {}  # dir:order
    check = [False] * len(edges)
    res = -1

    def dfs(node, step=0):
        nonlocal res
        # visited[node] = step
        nei = edges[node]
        if node == -1 or nei == -1 or check[node]: return
        if (node, nei) in visited:
            # print(node, nei, res, step, visited)
            res = max(res, step - visited[(node, nei)])
            return
        visited[(node, nei)] = step
        dfs(nei, step + 1)
        check[node] = True

    for i in range(len(edges)):
        dfs(i)
    return res


# bfs, topsort, TC:O(N), SC:O(N)
def longestCycle2(edges: List[int]) -> int:

    indegrees = {i: 0 for i in range(len(edges))}
    for a, b in enumerate(edges):
        if b == -1: continue
        indegrees[b] += 1
    queue = collections.deque([node for node, v in indegrees.items() if v == 0])
    while queue:  # topsort
        node = queue.popleft()
        # edges[node] = -1
        nei = edges[node]
        edges[node] = -1
        if nei == -1: continue
        indegrees[nei] -= 1
        if indegrees[nei] == 0:
            queue.append(nei)
    # print(edges)
    res = -1
    for s, t in enumerate(edges):
        if t == -1: continue
        step = 0
        stack = [s]
        while stack:
            node = stack.pop()
            if edges[node] == -1: continue
            step += 1
            nei = edges[node]
            stack.append(nei)
            edges[node] = -1
        res = max(res, step)
    return res