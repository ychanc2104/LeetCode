# https://leetcode.com/problems/minimum-height-trees/

import collections

# first thought, BFS, TC:O(n^2), time exceed
def findMinHeightTrees(n: int, edges):
    dict_map = collections.defaultdict(list)
    for i in range(len(edges)):
        x, y = edges[i]
        dict_map[x].append(y)
        dict_map[y].append(x)

    heights = []
    for i in range(n):
        queue = [i]
        height = 0
        visit = set()
        while queue:
            leafs = []
            for node in queue:
                if node not in visit:
                    leafs.extend(dict_map[node])
                    visit.add(node)
            queue = leafs
            height += 1
        heights.append(height)

    # print(heights)
    min_h = min(heights)
    res = []
    for i, h in enumerate(heights):
        if h == min_h:
            res.append(i)
    return res

# topsort, TC:O(V+E), SC:O(V+E)
def findMinHeightTrees2(n: int, edges):
    if n == 1:
        return [0]
    dict_map = collections.defaultdict(set)
    for i in range(len(edges)):
        x, y = edges[i]
        dict_map[x].add(y)
        dict_map[y].add(x)

    # print(dict_map, in_degrees)
    # remove from in_degree=1
    leaves = []
    for i in range(n):
        if len(dict_map[i]) == 1:
            leaves.append(i)

    n_nodes = n
    while n_nodes > 2:
        new_leaves = []
        n_nodes -= len(leaves)
        for l in leaves:
            neighbor = dict_map[l].pop()
            dict_map[neighbor].remove(l)
            if len(dict_map[neighbor]) == 1:
                new_leaves.append(neighbor)
        leaves = new_leaves
    # print(in_degrees, dict_map, leaves)
    return leaves


# topsort, TC:O(V+E), SC:O(V+E)
def findMinHeightTrees3(n: int, edges):
    if n <= 2: return [i for i in range(n)]
    graph = collections.defaultdict(set)
    for a,b in edges:
        # undirected
        graph[a].add(b)
        graph[b].add(a)
    # top sort
    drop = [node for node,neighbors in graph.items() if len(neighbors) == 1]
    count = n
    while count > 2:
        new_drop = []
        for node in drop:
            # drop neighbor of node, must be only one neighbor
            nei = graph[node].pop()
            graph[nei].remove(node) # remove node
            if len(graph[nei]) == 1:
                new_drop.append(nei) # attempt to drop
        count -= len(drop) # remaining node
        drop = new_drop
    return drop

# topsort, TC:O(V+E), SC:O(V+E)
def findMinHeightTrees4(n: int, edges):
    graph = collections.defaultdict(list)
    indegrees = {i:0 for i in range(n)}
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)
        indegrees[a] += 1
        indegrees[b] += 1
    # find outer
    queue = [n for n,v in indegrees.items() if v <= 1]
    while n > 2:
        n -= len(queue)
        leafs = []
        for node in queue:
            for nei in graph[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 1:
                    leafs.append(nei)
        queue = leafs
    return queue