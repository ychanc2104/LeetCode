# https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/
# https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/solutions/1097204/python-java-dijkstra-cached-dfs-clean-concise/

import collections, heapq

# Bellman-Ford + dp(TLE)
def countRestrictedPaths(n: int, edges: List[List[int]]) -> int:
    # build adjacency list
    graph = collections.defaultdict(list)
    for x, y, w in edges:
        graph[x].append((y, w))
        graph[y].append((x, w))
    # find min distance of each node to n
    dp = [float('inf')] * (n + 1)
    dp[-1] = 0
    queue = collections.deque([n])  # from n to relax
    while queue:
        node = queue.popleft()
        for nei, w in graph[node]:
            if dp[node] + w < dp[nei]:
                dp[nei] = dp[node] + w
                queue.append(nei)
            # if dp[y] + w < dp[x]:
            #     dp[x] = dp_prev[y] + w

    memo = {}  # dp, cache

    def dfs(i):  # How many decreasing array start with i
        if i == n: return 1
        if i in memo: return memo[i]
        s_path = 0
        for nei, w in graph[i]:  # node larger
            if dp[i] > dp[nei]:  # weight != 0
                s_path += dfs(nei)
        s_path %= (10 ** 9 + 7)
        memo[i] = s_path
        return s_path

    return dfs(1)


# Dijkstra + dp, TC:O(N^2logN), SC:O(N^2)
def countRestrictedPaths2(n: int, edges: List[List[int]]) -> int:
    # build adjacency list
    graph = collections.defaultdict(list)
    for x,y,w in edges:
        graph[x].append((y, w))
        graph[y].append((x, w))
    # find min distance of each node to n
    dp = [float('inf')] * (n+1)
    dp[-1] = 0
    heaps = [(0, n)] # from n to relax, dist
    while heaps:
        dist, node = heapq.heappop(heaps)
        if dist > dp[node]: continue # skip previous (optimization)
        for nei, w in graph[node]:
            if dp[node] + w < dp[nei]:
                dp[nei] = dp[node] + w
                heapq.heappush(heaps, (dp[node] + w, nei))

    memo = {}
    def dfs(i): # How many decreasing array start with i
        if i == n: return 1
        if i in memo: return memo[i]
        s_path = 0
        for nei,w in graph[i]: # node larger
            if dp[i] > dp[nei]: # weight != 0
                s_path += dfs(nei)
        s_path %= (10**9+7)
        memo[i] = s_path
        return s_path
    return dfs(1)