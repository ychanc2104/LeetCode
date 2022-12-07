# https://leetcode.com/problems/strange-printer-ii/
# https://leetcode.com/problems/strange-printer-ii/solutions/854219/java-topological-sort/

import collections

# topsort, TC:O(kMN) k is number of colors, SC:O(k)
def isPrintable(targetGrid: List[List[int]]) -> bool:
    # course schedule => add prerequistites
    # find boundary of each color
    boundary = collections.defaultdict(lambda: [float("inf"), float("inf"), float("-inf"), float("-inf")])
    n, m = len(targetGrid), len(targetGrid[0])
    for i in range(n):
        for j in range(m):
            color = targetGrid[i][j]
            mr, mc, Mr, Mc = boundary[color]
            boundary[color] = [min(mr, i), min(mc, j), max(Mr, i), max(Mc, j)]
    # build graph
    graph = collections.defaultdict(set)
    indegrees = {i: 0 for i in boundary.keys()}
    for pre, (mr, mc, Mr, Mc) in boundary.items():
        # add prerequisites
        for i in range(mr, Mr + 1):
            for j in range(mc, Mc + 1):
                color = targetGrid[i][j]
                if color == pre: continue
                if color not in graph[pre]:
                    indegrees[color] += 1
                graph[pre].add(color)
    # print(graph, indegrees)
    # do bfs
    queue = collections.deque([c for c, v in indegrees.items() if v == 0])
    count = len(indegrees.keys())
    while queue:
        color = queue.popleft()
        count -= 1
        for nei in graph[color]:
            indegrees[nei] -= 1
            if indegrees[nei] == 0:
                queue.append(nei)
    return count == 0

