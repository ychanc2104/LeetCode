# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/solutions/493629/java-floyd-spfa-dijkstra-and-bellman/


import collections

# first thought, Bellman-Ford, TC:O(N^4), SC:O(N^2)
def findTheCity(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    # dp[i][j]: min distance from i to j
    dp = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    res = []
    for i in range(n):
        for _ in range(n - 1):
            dp_prev = dp[i].copy()
            for x, y, w in edges: # edges ~ O(N^2)
                if dp_prev[x] + w < dp[i][y] and dp_prev[x] + w <= distanceThreshold:
                    dp[i][y] = dp_prev[x] + w  # update
                if dp_prev[y] + w < dp[i][x] and dp_prev[y] + w <= distanceThreshold:  # bi-drectional
                    dp[i][x] = dp_prev[y] + w  # update
        res.append(sum(x != float('inf') for x in dp[i]) - 1)
    print(dp, res)
    idx, m = 0, float('inf')
    for i, v in enumerate(res):
        if v <= m:
            m = v
            idx = i
    return idx
    # return min([(res[i], i) for i in range(n)], key=lambda x: [x[0], -x[1]])[1]

# optimized Bellman-Ford(build graph), TC:O(N^3), SC:O(N^2)
def findTheCity2(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    graph = collections.defaultdict(list)
    for x,y,w in edges: # TC:O(N^2), SC:O(N^2)
        graph[x].append((y,w))
        graph[y].append((x,w))
    res = []
    for i in range(n):
        queue = collections.deque([i])
        dp = [float('inf')] * n
        dp[i] = 0 # from i
        while queue: # TC:O(V+E) = O(N+N^2)
            city = queue.popleft()
            for nei,w in graph[city]:
                if dp[city] + w < dp[nei] and dp[city] + w <= distanceThreshold: # update
                    dp[nei] = dp[city] + w
                    queue.append(nei)
        res.append(sum(x!=float('inf') for x in dp))
    # print(res)
    # idx, m = 0, float('inf')
    # for i, v in enumerate(res):
    #     if v <= m:
    #         m = v
    #         idx = i
    # return idx
    return min([(res[i], i) for i in range(n)], key=lambda x: [x[0], -x[1]])[1]


# Floyd–Warshall algorithm, TC:O(N^3), SC:O(N^2)
def findTheCity3(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    dis = [[float('inf')] * n for _ in range(n)] # dis[i][j]: min distance from i to j
    for i, j, w in edges:
        dis[i][j] = dis[j][i] = w # without duplicates
    for i in range(n):
        dis[i][i] = 0 # init
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # dist(i to j) = min(dist(i to j), dist(i to k) + dist(k to j))
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
    # print(dis)
    res = {sum(d <= distanceThreshold for d in dis[i]): i for i in range(n)}
    return res[min(res)]