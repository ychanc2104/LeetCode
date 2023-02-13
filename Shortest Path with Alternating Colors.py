# https://leetcode.com/problems/shortest-path-with-alternating-colors/

import collections


# multi-source BFS, TC:O(N+M), SC:O(N+M)
def shortestAlternatingPaths(n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    graph_c = [collections.defaultdict(list) for _ in range(2)]  # 0:red, 1:blue
    for a, b in redEdges:
        graph_c[0][a].append((b, 1))  # to blue
    for a, b in blueEdges:
        graph_c[1][a].append((b, 0))  # to red
    # print(graph_c)

    res = [float('inf')] * n
    res[0] = 0  # self-edge
    queue = collections.deque([(0, 0, 0), (0, 1, 0)])  # node, color, path
    visited = [[False] * 2 for _ in range(n)]
    while queue:
        node, color, path = queue.popleft()
        if visited[node][color]: continue
        visited[node][color] = True
        res[node] = min(res[node], path)
        # print(node, color, graph_c[color][node])
        for nei, c in graph_c[color][node]:
            queue.append((nei, c, path + 1))
    return [x if x != float('inf') else -1 for x in res]