# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

import collections, heapq

# first thought, BFS, Bellman-Ford, TC:O(), SC:O()
def minScore(n: int, roads: List[List[int]]) -> int:
    graph = collections.defaultdict(list)
    for a, b, w in roads:
        graph[a].append((b, w))
        graph[b].append((a, w))

    dp = [float('inf')] * (n + 1)  # min score from 1 to i
    queue = collections.deque([(1, float('inf'))])
    while queue:
        node, score = queue.popleft()
        for nei, w in graph[node]:
            if min(score, w) < dp[nei]:
                dp[nei] = min(score, w)
                queue.append((nei, dp[nei]))
    return dp[-1]

# first thought, Dijkstra, TC:O(), SC:O()
def minScore2(n: int, roads: List[List[int]]) -> int:
    graph = collections.defaultdict(list)
    for a,b,w in roads:
        graph[a].append((b, w))
        graph[b].append((a, w))

    dp = [float('inf')] * (n+1) # min score from 1 to i
    heaps = [(float('inf'), 1)] # score, node
    while heaps:
        score, node = heapq.heappop(heaps)
        for nei, w in graph[node]:
            if min(score, w) < dp[nei]:
                dp[nei] = min(score, w)
                heapq.heappush(heaps, (dp[nei], nei))
    return dp[-1]

# simple dfs, TC:O(N+M), SC:O(N+M)
def minScore3(n: int, roads: List[List[int]]) -> int:
    graph = collections.defaultdict(list)
    for a, b, w in roads:
        graph[a].append((b, w))
        graph[b].append((a, w))
    # min score from 1 to every node
    res = float('inf')
    visited = set()

    def dfs(node):
        nonlocal res

        for nei, w in graph[node]:
            res = min(res, w)  # explore all edges
            if nei in visited: continue
            visited.add(nei)
            dfs(nei)

    dfs(1)
    return res

# union find, TC:O(N+M), SC:O(N+M)
def minScore4(n: int, roads: List[List[int]]) -> int:
    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]
    def union(x, y):
        px, py = find(x), find(y)
        parents[px] = py
    parents = [i for i in range(n+1)]
    res = float('inf')
    for a,b,_ in roads:
        union(a, b)
    p1 = find(1)
    for a,b,w in roads:
        if p1 == find(a): # same group
            res = min(res, w)
    return res