# https://leetcode.com/problems/number-of-operations-to-make-network-connected/


# first thought, union find, TC:O(N+M), SC:O(N)
def makeConnected(n: int, connections: List[List[int]]) -> int:
    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    parents = [i for i in range(n)]
    ava = 0
    for a, b in connections:
        pa, pb = find(a), find(b)
        if pa == pb:
            ava += 1
            continue
        parents[pa] = pb

    res = len(set([find(i) for i in range(n)])) - 1
    return res if ava >= res else -1


# concise union find, TC:O(N+M), SC:O(N)
def makeConnected2(n: int, connections: List[List[int]]) -> int:
    if len(connections) < n-1:
        return -1
    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]
    parents = [i for i in range(n)]
    components = n
    for a,b in connections:
        pa, pb = find(a), find(b)
        if pa == pb:
            continue
        parents[pa] = pb
        components -= 1
    return components-1