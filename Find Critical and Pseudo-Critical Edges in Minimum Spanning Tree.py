# https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/
# https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/solutions/1478180/python-mst-with-kruskal-s-algorithm-standard-code-clean-concise/


# minimum spanning tree, Kruskal's algorithm(union find), TC:O(M^2*alpha(N)) M is len of edges, SC:O(N+M) M for sorting
def findCriticalAndPseudoCriticalEdges(n: int, edges: List[List[int]]) -> List[List[int]]:
    def find(parents, x):
        if x != parents[x]:
            parents[x] = find(parents, parents[x])
        return parents[x]

    def union(parents, x, y):
        px, py = find(parents, x), find(parents, y)
        if px == py:
            return False
        parents[px] = py
        return True

    parents = [i for i in range(n)]
    # need to preserve original index
    edges = sorted([[a, b, w, i] for i, (a, b, w) in enumerate(edges)], key=lambda x: x[2])  # TC:O(MlogM), SC:O(M)

    # i_exclude and i_include is new index after sorting
    def kruskal(parents, i_exclude=None, i_include=None):  # TC:O(M*alpha(N))
        weight = 0
        group = len(parents)
        if i_include:  # union first
            a, b, w, _ = edges[i_include]
            union(parents, a, b)
            weight += w
            group -= 1
        for i, (a, b, w, _) in enumerate(edges):
            if i == i_exclude: continue  # skip this
            if union(parents, a, b):
                weight += w
                group -= 1
        return weight if group == 1 else float("inf")

    # find critical edges (must be existing)
    totalMST = kruskal(parents.copy())
    res_cri = []
    for i, (a, b, w, _) in enumerate(edges):  # TC:O(M^2)
        if totalMST < kruskal(parents.copy(), i_exclude=i):
            res_cri.append(edges[i][3])  # orginal index
    # find pseudo-critical edges (not include in res_cri and still MST and not redundant)
    cri_set = set(res_cri)
    res_pseu = []
    for i, (a, b, w, _) in enumerate(edges):  # TC:O(M^2)
        if edges[i][3] in cri_set: continue
        if totalMST == kruskal(parents.copy(), i_include=i):
            res_pseu.append(edges[i][3])  # orginal index
    return [res_cri, res_pseu]