# https://leetcode.com/problems/detonate-the-maximum-bombs/description/

import collections

# bfs, TC:O(N^3), SC:O(N^2)
def maximumDetonation(bombs: List[List[int]]) -> int:
    graph = collections.defaultdict(list)
    for i, (x1, y1, r1) in enumerate(bombs):  # TC:O(N)
        for j, (x2, y2, r2) in enumerate(bombs):  # TC:O(N)
            if i == j: continue
            if r1 ** 2 >= (x1 - x2) ** 2 + (y1 - y2) ** 2:
                graph[i].append(j)
    res = 0
    for i in range(len(bombs)):  # TC:O(N)
        queue = collections.deque([i])
        visit = set(queue)
        while queue:  # TC:O(N + N^2)
            node = queue.popleft()
            for adj in graph[node]:
                if adj in visit: continue
                queue.append(adj)
                visit.add(adj)
        res = max(res, len(visit))
    return res