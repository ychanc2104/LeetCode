# https://leetcode.com/problems/campus-bikes-ii/
# https://leetcode.com/problems/campus-bikes-ii/solutions/303422/python-priority-queue/
# https://leetcode.com/problems/campus-bikes-ii/solutions/833910/python3-dfs-lru-cache-campus-bikes-ii/


import heapq, functools

# use heaps ~ Dijkstra, TC:O(P(M,N)logP(M,N) + M*logP(M,N)*2^M), SC:O(P(M,N) + 2^M) P(M,N) is permutation of M,N for queue and 2^M for visited  ,N:len(worker), M:len(bikes)
def assignBikes(workers: List[List[int]], bikes: List[List[int]]) -> int:
    # heaps: [distance, remain_worker, remain_bike]

    heaps = [(0, 0, 0)]  # dist, i_worker, bike_status (000000, bit mask)
    visited = set()
    dist = lambda x, y: abs(workers[x][0] - bikes[y][0]) + abs(workers[x][1] - bikes[y][1])
    while heaps: 
        d, i, bike_status = heapq.heappop(heaps) # TC:O(P(M,N)logP(M,N))
        if bike_status in visited: continue # don't visit same status twice
        visited.add(bike_status)
        if i == len(workers): return d
        for j in range(len(bikes)): # TC:O(M*logP(M,N)*2^M)
            if (1 << j) & bike_status: continue  # same bike
            heapq.heappush(heaps, (d + dist(i, j), i + 1, bike_status | (1 << j)))  # occupied bike j


# top-down dp+dfs, TC:O(M*2^M), SC:O(2^M)
def assignBikes2(workers: List[List[int]], bikes: List[List[int]]) -> int:
    n, m = len(workers), len(bikes)
    dist = lambda x,y: abs(workers[x][0]-bikes[y][0]) + abs(workers[x][1]-bikes[y][1])
    @functools.lru_cache(None)
    def dfs(i_worker:int, bike_status:int):
        if i_worker == n: return 0
        res = float('inf')
        for j in range(m):
            if bike_status & 1<<j: continue # same bike
            res = min(res, dist(i_worker, j) + dfs(i_worker+1, bike_status | (1<<j)))
        return res
    return dfs(0, 0)

# top-down dp+dfs, TC:O(M*2^M), SC:O(2^M)
def assignBikes3(workers: List[List[int]], bikes: List[List[int]]) -> int:
    n, m = len(workers), len(bikes)
    dist = lambda x, y: abs(workers[x][0] - bikes[y][0]) + abs(workers[x][1] - bikes[y][1])
    dp = {} # min sum distance at given bike_status
    def dfs(i_worker: int, bike_status: int):
        if i_worker == n: return 0
        if bike_status in dp: return dp[bike_status]
        res = float('inf')
        for j in range(m):
            if bike_status & 1 << j: continue  # same bike
            res = min(res, dist(i_worker, j) + dfs(i_worker + 1, bike_status | (1 << j)))
        dp[bike_status] = res
        return res

    return dfs(0, 0)