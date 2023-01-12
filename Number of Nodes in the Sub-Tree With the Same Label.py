# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

import collections


# dfs, TC:O(N), SC:O(N)
def countSubTrees(n: int, edges: List[List[int]], labels: str) -> List[int]:
    res = [0] * n

    def dfs(node=0, parent=-1):  # return counter
        counter = collections.Counter(labels[node])
        for child in graph[node]:
            if parent == child: continue  # do not go back
            counter += dfs(child, node)
        res[node] += counter[labels[node]]
        return counter

    graph = collections.defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    dfs()
    return res


# dfs, TC:O(N), SC:O(N)
def countSubTrees2(n: int, edges: List[List[int]], labels: str) -> List[int]:
    res = [0] * n
    visited = [False] * n
    visited[0] = True

    def dfs(node=0):  # return counter
        counter = collections.Counter(labels[node])
        for child in graph[node]:
            if visited[child]: continue
            visited[child] = True
            counter += dfs(child)
        res[node] += counter[labels[node]]
        return counter

    graph = collections.defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    dfs()
    return res

# dfs, TC:O(N), SC:O(N)
def countSubTrees3(n: int, edges: List[List[int]], labels: str) -> List[int]:

    res = [0] * n
    visited = [False] * n
    def dfs(node=0): # return counter
        if visited[node]:
            return collections.Counter()
        visited[node] = True
        counter = collections.Counter(labels[node])
        for child in graph[node]:
            counter += dfs(child)
        res[node] += counter[labels[node]]
        return counter
    graph = collections.defaultdict(list)
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)
    dfs()
    return res