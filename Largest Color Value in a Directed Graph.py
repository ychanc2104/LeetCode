# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/
# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/solutions/1198908/python-shortest-code-and-fast/

import collections

# topsort + dp, TC:O(N+M) N is len colors and M is len of edges, SC:O(N+M)
def largestPathValue(colors: str, edges: List[List[int]]) -> int:
    # build graph => add counter to do bfs
    graph = collections.defaultdict(list)
    indegrees = {i: 0 for i in range(len(colors))}
    dp = [[0] * 26 for _ in range(len(colors))]  # dp[node]: all max possible count reaching node
    for a, b in edges:
        graph[a].append(b)
        indegrees[b] += 1
    queue = collections.deque([n for n, c in indegrees.items() if c == 0])
    # print(queue, graph)
    count = len(colors)
    while queue:
        node = queue.popleft()
        count -= 1
        dp[node][ord(colors[node]) - ord('a')] += 1
        for nei in graph[node]:
            dp[nei] = [max(x, y) for x, y in zip(dp[node], dp[nei])]  # store all possible counts
            indegrees[nei] -= 1
            if indegrees[nei] == 0:
                queue.append(nei)  #
    return max(c for cnt in dp for c in cnt) if count == 0 else -1


# dfs, TC:O(N+M), SC:O(N+M)
def largestPathValue2(colors: str, edges: List[List[int]]) -> int:

    graph = collections.defaultdict(list)
    for a,b in edges:
        graph[a].append(b)
    n = len(colors)
    counter = [[0]*26 for _ in range(n)] # counter[i]: all possible max frequency start with i
    visited = [False] * n
    inPath = [False] * n
    def dfs(node):
        if inPath[node]:
            return float('inf')
        if visited[node]: # use cache
            return counter[node][ord(colors[node]) - ord('a')]
        inPath[node] = True
        visited[node] = True
        for nei in graph[node]:
            if dfs(nei) == float('inf'):
                return float('inf')
            for i in range(26):
                counter[node][i] = max(counter[node][i], counter[nei][i])

        counter[node][ord(colors[node]) - ord('a')] += 1
        inPath[node] = False
        return max(counter[node])

    res = 0
    for i in range(n):
        res = max(res, dfs(i))
    return res if res != float('inf') else -1

# dfs, TC:O(N+M), SC:O(N+M)
def largestPathValue3(colors: str, edges: List[List[int]]) -> int:

    graph = collections.defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
    n = len(colors)
    counter = [collections.Counter() for _ in range(n)]  # max counter start with i
    visited = [False] * n
    inPath = [False] * n

    def dfs(node):
        if inPath[node]:
            return float('inf')
        if visited[node]:  # use cache
            return counter[node][colors[node]]
        inPath[node] = True
        visited[node] = True

        for nei in graph[node]:
            if dfs(nei) == float('inf'):
                return float('inf')
            for k in counter[nei].keys():  # update counter[node]
                counter[node][k] = max(counter[node][k], counter[nei][k])
        counter[node][colors[node]] += 1  # post-order
        inPath[node] = False
        return max(counter[node].values())

    res = 0
    for i in range(n):
        res = max(res, dfs(i))
    return res if res != float('inf') else -1