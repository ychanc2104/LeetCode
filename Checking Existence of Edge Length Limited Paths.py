# https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/
# https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/solutions/978576/python3-union-find/

# union find, TC:O(NlogN+MlogM), SC:O(N+M)
def distanceLimitedPathsExist(n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
    # sort by weight and limit
    # union all nodes from lowest weight

    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        px, py = find(x), find(y)
        parents[px] = py

    parents = [i for i in range(n)]
    queries2 = sorted([(l, p, q, i) for i, (p, q, l) in enumerate(queries)]) # TC:O(mlogm), SC:O(m)
    edgeList2 = sorted([(w, p, q) for p, q, w in edgeList]) # TC:O(nlogn), SC:O(n)

    res = [False] * len(queries)  # need to keep original index
    i = 0
    for l, p, q, idx in queries2:
        while i < len(edgeList) and edgeList2[i][0] < l:
            w, node1, node2 = edgeList2[i]
            union(node1, node2)
            i += 1

        res[idx] = (find(p) == find(q))
    return res