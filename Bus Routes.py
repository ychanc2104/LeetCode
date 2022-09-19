# https://leetcode.com/problems/bus-routes/

import collections

# first thought (TLE),
def numBusesToDestination(routes: List[List[int]], source: int, target: int) -> int:
    if source == target:
        return 0
    # build adjacency list
    adj = collections.defaultdict(set)
    routes_set = [set(r) for r in routes]
    for i, route in enumerate(routes):
        for j in range(i + 1, len(routes)):
            if i == j:
                continue
            if any([s in routes_set[j] for s in route]):
                # add index of bus
                adj[i].add(j)
                adj[j].add(i)

    # print(adj)
    # bfs
    queue = [i for i in range(len(routes)) if source in routes[i]]
    target = set([i for i in range(len(routes)) if target in routes[i]])
    visit = set(queue)
    res = 1
    while queue:
        # collecting all neighbors
        neighbors = []
        for bus in queue:
            if bus in target:
                return res
            # visit.add(bus)
            for d in adj[bus]:
                if d in visit:
                    continue
                visit.add(d)
                neighbors.append(d)
        res += 1
        queue = neighbors
    return -1

# ,
def numBusesToDestination2(routes: List[List[int]], source: int, target: int) -> int:
    # use a queue to manage what the next stops to visit in a generation are
    # when we visit a stop, the next stop can be any stop in a route containing this stop
    # since we propagate like this, we mark any route that we've already checked as visited
    # if the route hasnt been visited, we append all stops in the route to the end of the queue

    if source == target:
        return 0

    # {stop: [list of route numbers that this stop is in]}
    routeMap = collections.defaultdict(list)
    for routeIndex, route in enumerate(routes):
        for stop in route:
            routeMap[stop].append(routeIndex)

    numBuses = 0
    queue = collections.deque([source])
    visited = set()

    while queue:
        numBuses += 1
        numInCurrGen = len(queue)
        for i in range(numInCurrGen):
            currStop = queue.popleft()
            for routeIndex in routeMap[currStop]:
                if routeIndex not in visited:
                    for stop in routes[routeIndex]:
                        if stop == target:
                            return numBuses
                        queue.append(stop)
                    visited.add(routeIndex)

    return -1



# ,
def numBusesToDestination3(routes: List[List[int]], source: int, target: int) -> int:
    to_routes = collections.defaultdict(set)
    for i, route in enumerate(routes):
        for j in route:
            to_routes[j].add(i)
    bfs = [(source, 0)]
    seen = set([source])
    for stop, bus in bfs:
        if stop == target: return bus
        for i in to_routes[stop]:
            for j in routes[i]:
                if j not in seen:
                    bfs.append((j, bus + 1))
                    seen.add(j)
            routes[i] = []  # seen route
    return -1

# bfs, TC:O(NM), SC:O(NM)
def numBusesToDestination4(routes: List[List[int]], source: int, target: int) -> int:
    # use a queue to manage what the next stops to visit in a generation are
    # when we visit a stop, the next stop can be any stop in a route containing this stop
    # since we propagate like this, we mark any route that we've already checked as visited
    # if the route hasnt been visited, we append all stops in the route to the end of the queue

    if source == target:
        return 0

    # {stop: [list of route numbers that this stop is in]}
    # TC:O(nm), n is len(routes), m is average stops in bus
    routeMap = collections.defaultdict(list)
    for routeIndex, route in enumerate(routes):
        for stop in route:
            routeMap[stop].append(routeIndex)

    res = 0
    queue = collections.deque([source])
    visited = set() # store visited bus
    # TC:O(V+E) = O(N + NM)
    while queue:
        neighbors = []
        for stop in queue:
            if stop == target: return res
            for i in routeMap[stop]:
                # all bus contain stop
                if i in visited:
                    continue
                for s in routes[i]:
                    neighbors.append(s)
                visited.add(i) # mark this bus visited
        queue = neighbors
        res += 1
    return -1