# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description/
# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/solutions/2357694/two-dfs/


# two dfs(bfs is same because only one outgoing node), TC:O(N), SC:O(N)
def closestMeetingNode(edges: List[int], node1: int, node2: int) -> int:
    # [0,-1,1,2] and [-1,0,1,2]
    n = len(edges)
    d1 = [-1] * n
    d1[node1] = 0
    d2 = [-1] * n
    d2[node2] = 0

    def dfs(node, d):
        nei = edges[node]
        if nei != -1 and d[nei] == -1: # can reach and not visited yet
            d[nei] = d[node] + 1
            dfs(nei, d)

    # print(d1, d2)
    dfs(node1, d1)
    dfs(node2, d2)
    # print(d1, d2)
    res = -1
    d_min = float('inf')
    for i, (v1, v2) in enumerate(zip(d1, d2)):
        if v1 == -1 or v2 == -1:  # skip
            continue
        if d_min > max(v1, v2):  # minimize max distance
            res = i
            d_min = max(v1, v2)
    return res