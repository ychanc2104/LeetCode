# https://leetcode.com/problems/path-with-maximum-probability/
# https://leetcode.com/problems/path-with-maximum-probability/solutions/731767/java-python-3-2-codes-bellman-ford-and-dijkstra-s-algorithm-w-brief-explanation-and-analysis/

import collections, heapq

# Bellman-Ford, bfs + dp, TC:O(NM+N^2) ~ O(NM) M is len of edges ~ N-1, SC:O(N)
def maxProbability(n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
    # bellman-ford
    dp = [0] * n
    dp[start] = 1
    while True:
        dp_prev = dp.copy() # TC:O(N)
        stop = True  # flag
        for p, (a, b) in zip(succProb, edges):
            if p * dp_prev[a] > dp[b]: # bi-directional
                # update
                dp[b] = dp_prev[a] * p
                stop = False
            if p * dp_prev[b] > dp[a]: # bi-directional
                dp[a] = dp_prev[b] * p
                stop = False
        if stop: break
    return dp[end]


# Bellman-Ford, bfs + dp, TC:O(NM) M is len of edges, SC:O(N+M)
def maxProbability2(n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
    # bellman-ford
    graph, queue = collections.defaultdict(list), collections.deque([start])
    for i, (a, b) in enumerate(edges):
        graph[a].append([b, i])
        graph[b].append([a, i])
    dp = [0.0] * n
    dp[start] = 1.0
    while queue:
        cur = queue.popleft()
        for neighbor, i in graph[cur]:
            if dp[cur] * succProb[i] > dp[neighbor]:
                dp[neighbor] = dp[cur] * succProb[i]
                queue.append(neighbor)
    return dp[end]


# Dijkstra, TC:O((|V|+|E|)*log(|V|)) = O((N+M)logM), SC:O(N+M)
def maxProbability3(n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
    graph = collections.defaultdict(list)
    for i, (a, b) in enumerate(edges):
        graph[a].append([b, i])
        graph[b].append([a, i])
    dp = [0.0] * n
    dp[start] = 1.0
    heaps = [(-dp[start], start)]
    while heaps:
        p_cur, cur = heapq.heappop(heaps) # start from max prob.
        if cur == end: return -p_cur
        for neighbor, i in graph[cur]: # explore
            if -p_cur * succProb[i] > dp[neighbor]: # find larger path
                dp[neighbor] = -p_cur * succProb[i] # update
                heapq.heappush(heaps, (-dp[neighbor], neighbor)) # push to heaps
    return 0.0