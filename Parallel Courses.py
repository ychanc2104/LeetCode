# https://leetcode.com/problems/parallel-courses/

import collections

# topsort, TC:O(N+M) M is len of relations, SC:O(N)
def minimumSemesters(n: int, relations: List[List[int]]) -> int:
    indegrees = collections.defaultdict(int)
    graph = collections.defaultdict(list)
    for pre, cur in relations:
        indegrees[cur] += 1
        indegrees[pre] += 0
        graph[pre].append(cur)

    queue = [c for c, v in indegrees.items() if v == 0]
    count = 0
    while queue:
        leafs = []
        n -= len(queue)  # take classes
        for node in queue:
            for nei in graph[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    leafs.append(nei)
        queue = leafs
        count += 1
    for v in indegrees.values():  # if not all indegrees == 0, return -1
        if v != 0:
            return -1
    # print(count, n)
    return count


# topsort, TC:O(N+M) M is len of relations(edges), SC:O(N+M)
def minimumSemesters2(n: int, relations: List[List[int]]) -> int:
    indegrees = {i: 0 for i in range(1, n + 1)} # SC:O(N)
    graph = collections.defaultdict(list) # SC:O(M)
    for pre, cur in relations:
        indegrees[cur] += 1
        graph[pre].append(cur)
    queue = [c for c, v in indegrees.items() if v == 0]
    count = 0
    while queue:
        leafs = []
        n -= len(queue)  # take classes
        for node in queue:
            for nei in graph[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    leafs.append(nei)
        queue = leafs
        count += 1
    return count if n == 0 else -1