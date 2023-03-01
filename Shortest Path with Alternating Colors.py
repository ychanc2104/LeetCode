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



# concise multi-source BFS, TC:O(N+M), SC:O(N+M)
def shortestAlternatingPaths2(n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

    graph_c = [collections.defaultdict(list) for _ in range(2)]  # 0:red, 1:blue
    for a, b in redEdges:
        graph_c[0][a].append(b)  # to blue
    for a, b in blueEdges:
        graph_c[1][a].append(b)  # to red
    # print(graph_c)

    res = [[float('inf')] * 2 for _ in range(n)]
    res[0] = [0, 0]
    queue = collections.deque([(0, 0), (0, 1)])  # node, color
    while queue:
        node, color = queue.popleft()
        for nei in graph_c[color][node]:
            next_color = 1 - color
            if res[nei][next_color] != float('inf'): continue
            res[nei][next_color] = res[node][color] + 1
            queue.append((nei, next_color))
    return [min(x) if min(x) != float('inf') else -1 for x in res]