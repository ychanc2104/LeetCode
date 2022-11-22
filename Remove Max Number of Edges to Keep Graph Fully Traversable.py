# https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/?envType=study-plan&id=graph-ii

# first thought, union find, TC:O(NlogN + alpha(N)*N), SC:O(N)
def maxNumEdgesToRemove(n: int, edges: List[List[int]]) -> int:
    # remove redundant nodes
    edges.sort(key=lambda x: -x[0]) # consider type 3 first
    parents_a = [i for i in range(n)]
    parents_b = [i for i in range(n)]

    def find(parents, x):
        if x != parents[x]:
            parents[x] = find(parents, parents[x])
        return parents[x]

    res = 0
    for t, u, v in edges:
        u, v = u - 1, v - 1
        if t == 3:
            pu_a, pv_a = find(parents_a, u), find(parents_a, v)
            pu_b, pv_b = find(parents_b, u), find(parents_b, v)
            if pu_a == pv_a and pu_b == pv_b:
                res += 1
                continue
            parents_a[pu_a] = pv_a
            parents_b[pu_b] = pv_b
        elif t == 2:
            pu_b, pv_b = find(parents_b, u), find(parents_b, v)
            if pu_b == pv_b:
                res += 1
                continue
            parents_b[pu_b] = pv_b
        elif t == 1:
            pu_a, pv_a = find(parents_a, u), find(parents_a, v)
            if pu_a == pv_a:
                res += 1
                continue
            parents_a[pu_a] = pv_a

    for i in range(n):
        find(parents_a, i)
        find(parents_b, i)

    return res if len(set(parents_a)) == 1 and len(set(parents_b)) == 1 else -1

# do not sort, union find
def maxNumEdgesToRemove2(n: int, edges: List[List[int]]) -> int:
    # remove redundant nodes
    parents_a = [i for i in range(n)]
    parents_b = [i for i in range(n)]

    def find(parents, x):
        if x != parents[x]:
            parents[x] = find(parents, parents[x])
        return parents[x]

    def union(parents, x, y):
        px, py = find(parents, x), find(parents, y)
        if px == py:
            return False  # false union
        parents[px] = py
        return True

    res = 0
    n_conn_a = n_conn_b = 0  # edge counts
    # first to connect type 3
    for t, u, v in edges:
        u, v = u - 1, v - 1
        if t == 3:
            bool_a = union(parents_a, u, v)
            bool_b = union(parents_b, u, v)
            if not bool_a and not bool_b:
                res += 1
            if bool_a:
                n_conn_a += 1
            if bool_b:
                n_conn_b += 1
    for t, u, v in edges:
        u, v = u - 1, v - 1
        if t == 1:  # Alice
            if not union(parents_a, u, v):
                res += 1
            else:
                n_conn_a += 1
        elif t == 2:  # Bob
            if not union(parents_b, u, v):
                res += 1
            else:
                n_conn_b += 1
    return res if n_conn_a == n_conn_b == n - 1 else -1