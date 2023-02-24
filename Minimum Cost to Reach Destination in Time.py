# https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/
# https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/solutions/1421809/python3-easy-bellman-ford-solution/

import collections, heapq

# dp(Bellman-Ford) TLE, TC:O(TM) T is maxTime and M is len of edges, SC:O(TM)
def minCost(maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
    graph = collections.defaultdict(list)
    for x, y, t in edges:
        graph[x].append((y, t))
        graph[y].append((x, t))
    n = len(passingFees)
    dp = [[float("inf")] * n for _ in range(maxTime + 1)]  # dp[t][x]: min cost to x at given t limit
    dp[0][0] = passingFees[0]
    for t in range(maxTime + 1):
        for x, y, time in edges:
            if t < time: continue
            dp[t][x] = min(dp[t][x], dp[t - time][y] + passingFees[x])  # y to x
            dp[t][y] = min(dp[t][y], dp[t - time][x] + passingFees[y])  # x to y
    ans = min(dp[i][-1] for i in range(maxTime + 1))
    return ans if ans != float("inf") else -1

# Dijkstra + dp, TC:O(N+MlogM), SC:(N+M)
def minCost2(maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
    graph = collections.defaultdict(list)
    for x,y,t in edges: # TC:O(M), SC:O(M)
        graph[x].append((y,t))
        graph[y].append((x,t))
    n = len(passingFees)
    heaps = [(passingFees[0], 0, 0)] # fee,time,node
    times = [float("inf")] * n # min time of each node, TC:O(N), SC:O(N)
    times[0] = 0
    # put less time and less cost into heaps
    while heaps: # TC:O(MlogM), SC:O(M)
        fee, time, node = heapq.heappop(heaps)
        if node == n-1: return fee
        for nei,t in graph[node]: # to next city nei
            if time + t > maxTime: continue # skip
            if times[nei] > time + t: # decrease time
                heapq.heappush(heaps, (fee + passingFees[nei], time + t, nei))
                times[nei] = time + t # update min times
    return -1