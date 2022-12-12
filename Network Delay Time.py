# https://leetcode.com/problems/network-delay-time/

import collections

# first thought, Bellman-Ford, TC:O(NM+N^2) M is len of times, SC:O(N)
def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    # bellman ford
    dp = [float("inf")] * (n + 1)  # dp[i]: min time to reach i
    dp[0] = 0
    dp[k] = 0
    while True:
        stop = True
        dp_prev = dp.copy()
        for u, v, w in times:
            if dp_prev[u] + w < dp[v]:
                # update
                dp[v] = dp_prev[u] + w
                stop = False
        if stop: break
    res = max(x for x in dp)
    return res if res != float("inf") else -1


#Bellman-Ford, TC:O(N+M) M is len of times, SC:O(N+M)
def networkDelayTime2(times: List[List[int]], n: int, k: int) -> int:
    graph = collections.defaultdict(list)
    for u,v,w in times: # TC:O(M)
        graph[u].append((v, w)) # SC:O(M)
    # bellman ford
    dp = [float("inf")] * (n+1) # dp[i]: min time to reach i, SC:O(N)
    dp[0] = 0
    dp[k] = 0
    queue = collections.deque([(k, 0)]) # node, time
    while queue: # TC:O(N+M), SC:O(M)
        node, time = queue.popleft()
        for nei,w in graph[node]:
            if dp[nei] > dp[node] + w:
                dp[nei] = dp[node] + w
                queue.append((nei, dp[nei]))
    res = max(x for x in dp) # TC:O(N)
    return res if res!=float("inf") else -1