# https://leetcode.com/problems/redundant-connection/description/

import collections

# first thought bfs(Kahn's algorithm), TC:O(N), SC:O(N)
def findRedundantConnection(edges: List[List[int]]) -> List[int]:
    # check from the bottom
    # drop out indegree == 1, and check from the bottom return first indegree==2
    n = len(edges)
    indegree = collections.defaultdict(int)
    graph = collections.defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
        indegree[a] += 1
        indegree[b] += 1
    # find indegree == 1
    queue = collections.deque([i for i, v in indegree.items() if v == 1])
    while queue:
        node = queue.popleft()
        indegree[node] -= 1
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 1:
                queue.append(nei)
    # print(indegree)
    for a, b in edges[::-1]:
        if indegree[a] == 2 and indegree[b]:
            return [a, b]

# union find, TC:O(N*alpha), SC:O(N)
def findRedundantConnection2(edges: List[List[int]]) -> List[int]:
    parents = [i for i in range(len(edges))]
    rank = [0] * len(edges)

    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px == py: return False
        if rank[px] > rank[py]:
            parents[py] = px
        elif rank[px] < rank[py]:
            parents[px] = py
        else:
            parents[px] = py
            rank[py] += 1
        return True

    for a, b in edges:
        if not union(a - 1, b - 1):
            return a, b