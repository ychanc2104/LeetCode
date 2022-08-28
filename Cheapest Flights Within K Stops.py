# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/317262/2-Clean-Python-Solution-(BFS-Dijkstra-Explained)
# https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/686906/Python-Multipass-BFS-O(V2)-%2B-Dijkstra-with-SortedList-explained
# https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/662812/C%2B%2B-BFS-or-Bellman-Ford-Algo-or-Dijkstra-Algo

import collections, functools, heapq

# first thought, dfs (time limit exceeded)
def findCheapestPrice(n: int, flights , src: int, dst: int, k: int) -> int:
    visit = set()
    res = [float("inf")]
    @functools.lru_cache(None)
    def dfs(city, sum_price, count=0):
        if city in visit or count > k + 1 or sum_price >= res[0]:
            return
        if city == dst:
            res[0] = min(res[0], sum_price)
            return
        print(city)

        visit.add(city)
        for stop, price in graph[city]:
            dfs(stop, sum_price + price, count + 1)
        visit.remove(city)

    graph = collections.defaultdict(list)
    for start, end, price in flights:
        graph[start].append([end, price])

    dfs(src, 0, 0)
    return -1 if res[0] == float("inf") else res[0]

# first thought, bfs (time limit exceeded)
def findCheapestPrice2(n: int, flights , src: int, dst: int, k: int) -> int:    # BFS
    graph = collections.defaultdict(list)
    for s, d, p in flights:
        graph[s].append((d, p))

    res = float("inf")
    queue = [(src, 0, 0)]  # (node, count, sumPrice)
    while queue:
        node, count, sumPrice = queue.pop(0)
        if node == dst:
            res = min(res, sumPrice)
            continue
        if count > k or sumPrice >= res:
            # early return
            continue
        for neighbor, price in graph[node]:
            queue.append((neighbor, count + 1, sumPrice + price))
    return res if res != float("inf") else -1


# Bellman-Ford, bfs + dp, TC:O(|E|K), SC:O(N)
def findCheapestPrice3(n: int, flights , src: int, dst: int, k: int) -> int:
    # Bellman-Ford
    res = [float("inf")] * n
    res[src] = 0
    #
    for i in range(k + 1):
        temp = res.copy()
        for s, d, p in flights:  # O(E), E is number of edges
            # start from src
            if res[src] == float("inf"):
                continue
            if temp[s] + p < res[d]:
                # update res[d] if shorter path appeared
                res[d] = temp[s] + p
    return res[dst] if res[dst] != float("inf") else -1

# modified bfs + dp, use an array to store res, TC:O(|E|+|V|^2), SC:O(|E|)
def findCheapestPrice4(n: int, flights , src: int, dst: int, k: int) -> int:    # BFS
    # BFS
    graph = collections.defaultdict(list)
    # dp memo
    ans = [float("inf") for _ in range(n)]
    ans[src] = 0
    for s, d, p in flights:
        graph[s].append((d, p))

    queue = collections.deque([(src, 0, 0)])  # scr, stops, price
    while queue:
        city, stops, cost = queue.popleft()
        if stops > k:
            continue
        for neighbor, price in graph[city]:
            if cost + price < ans[neighbor]:
                # update ans
                ans[neighbor] = cost + price
                # do bfs
                queue.append((neighbor, stops + 1, cost + price))

    return ans[dst] if ans[dst] != float('inf') else -1


# Dijkstra, use priority queue(TLE), TC:O((|V|+|E|)*log(|V|)), SC:O(|V|)
def findCheapestPrice5(n: int, flights , src: int, dst: int, k: int) -> int:
    graph = collections.defaultdict(list)
    for s, d, p in flights:
        graph[s].append((d, p))
    heap = [(0, src, 0)] # cost, city, count
    while heap:
        # min heap to pop out min
        cost, city, count = heapq.heappop(heap)
        if city == dst:
            return cost
        if count > k:
            continue

        for neighbor, price in graph[city]:
            heapq.heappush(heap, (price + cost, neighbor, count+1))
    return -1

# optimized Dijkstra, TC:O((|V|+|E|)*log(|V|)), SC:O(|V|)
def findCheapestPrice5(n: int, flights , src: int, dst: int, k: int) -> int:
    graph = collections.defaultdict(list)
    for s, d, p in flights:
        graph[s].append((d, p))
    # Shortest distances array
    distances = [float("inf") for _ in range(n)]
    current_stops = [float("inf") for _ in range(n)]
    distances[src] = 0
    current_stops[src] = 0
    # (cost, city, count)
    heap = [(0, src, 0)]
    while heap:
        # min heap to pop out min
        cost, city, count = heapq.heappop(heap)
        if city == dst:
            return cost
        if count > k:
            continue
        # Examine and relax all neighboring edges if possible
        for neighbor, price in graph[city]:
            # better cost?
            if price + cost < distances[neighbor]:
                distances[neighbor] = price + cost
                heapq.heappush(heap, (price + cost, neighbor, count+1))
                current_stops[neighbor] = count
            # better step?
            elif count < current_stops[neighbor]:
                heapq.heappush(heap, (price + cost, neighbor, count+1))
    return -1

n = 17
flights = [[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]]
src = 13
dst = 4
k = 13

res = findCheapestPrice(n, flights , src, dst, k)
res4 = findCheapestPrice4(n, flights , src, dst, k)

res5 = findCheapestPrice5(n, flights , src, dst, k)