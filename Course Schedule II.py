# https://leetcode.com/problems/course-schedule-ii/
# https://leetcode.com/problems/course-schedule-ii/discuss/266867/Python-Topological-Sort-BFS-and-DFS-(reserve-order)

import collections

# use in_degrees (Kahn’s algorithm), TC:O(V+N), SC:O(V+N)
def findOrder(numCourses: int, prerequisites):
    graph = collections.defaultdict(list)
    # O(n)
    in_degrees = {i: 0 for i in range(numCourses)}
    # O(V)
    for c, p in prerequisites:
        graph[p].append(c)
        in_degrees[c] += 1
    # print(graph, in_degrees)
    res = []
    # collect initial nodes to be removed
    removes = collections.deque([])
    # O(n)
    for k, v in in_degrees.items():
        if v == 0:
            removes.append(k)
            in_degrees[k] = -1
    # O(n+V), topsort
    while removes:
        node = removes.popleft()
        res.append(node)
        # print(node, res, in_degrees)
        # iterate all edges
        for neighbor in graph[node]:
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0:
                removes.append(neighbor)
                in_degrees[neighbor] -= 1

    # print(in_degrees)
    # check whether exist a cycle or not
    return res if len(res) == numCourses else []

# dfs
def findOrder2(numCourses: int, prerequisites):
    G = [set() for _ in range(numCourses)]
    for d, s in prerequisites:
        G[s].add(d)
    vis, orders = [0] * numCourses, []

    def dfs_circle(x):
        vis[x] = -1
        for y in G[x]:
            if vis[y] < 0 or (not vis[y] and dfs_circle(y)):
                return True
        vis[x] = 1
        orders.append(x)
        return False

    for x in range(numCourses):
        if not vis[x] and dfs_circle(x):
            return []
    return orders[::-1]