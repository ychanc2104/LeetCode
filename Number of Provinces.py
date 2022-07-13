# https://leetcode.com/problems/number-of-provinces/
#

# union-find, TC:O(n^2), SC:O(n)
def findCircleNum(isConnected) -> int:
    parent = list(range(len(isConnected)))

    def ufind(x):
        if x != parent[x]:
            parent[x] = ufind(parent[x])
        return parent[x]

    def union(x, y):
        px, py = ufind(x), ufind(y)
        parent[px] = py

    for i in range(len(isConnected)):
        for j in range(i + 1, len(isConnected[0])):
            if isConnected[i][j] == 1:
                union(i, j)
    # node reduction
    for i in range(len(isConnected)):
        ufind(i)
    return len(set(parent))


# dfs, TC:O(n^2), SC:O(n)
def findCircleNum2(isConnected) -> int:
    visit = set()
    def dfs(i):
        for j in range(len(isConnected)):
            if j not in visit and isConnected[i][j] == 1:
                visit.add(j)
                dfs(j)
    res = 0
    for i in range(len(isConnected)):
        if i not in visit:
            res += 1
            dfs(i)
            # print(visit)
    return res


# union-find, TC:O(n^2), SC:O(n)
class UnionFind:
    def __init__(self, n):
        self.u = list(range(n))

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb: self.u[ra] = rb

    def find(self, a):
        while self.u[a] != a: a = self.u[a]
        return a


def findCircleNum(M):
    """
    :type M: List[List[int]]
    :rtype: int
    """

    if not M: return 0
    s = len(M)

    uf = UnionFind(s)
    for r in range(s):
        for c in range(r, s):
            if M[r][c] == 1: uf.union(r, c)

    return len(set([uf.find(i) for i in range(s)]))



isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]

res = findCircleNum(isConnected)
