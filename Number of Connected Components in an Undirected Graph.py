# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/discuss/319459/Python3-UnionFindDFSBFS-solution

import collections


# first thought, union-find, TC:O(E*alpha(n)) alpha(n) is inverse Ackermann function, SC:O(n)
def countComponents(n: int, edges) -> int:
    # union-find
    parent = [i for i in range(n)]

    # find and re-assign parent
    def find(x):
        px = parent[x]
        if x != px:
            parent[x] = find(px)
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        parent[px] = py

    for a, b in edges:
        union(a, b)

    for i in range(n):
        find(i)

    return len(set(parent))


# dfs, TC:O(V+E), SC:O(V+E), E for graph, V for visit
def countComponents2(n: int, edges) -> int:
    # build graph
    graph = collections.defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visit = set()

    def dfs(i):
        if i in visit:
            return
        visit.add(i)
        for neighbor in graph[i]:
            dfs(neighbor)

    res = 0
    for i in range(n):
        if i not in visit:
            dfs(i)
            res += 1
    return res
