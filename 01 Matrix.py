# https://leetcode.com/problems/01-matrix/
# https://leetcode.com/problems/01-matrix/discuss/1369741/C%2B%2BJavaPython-BFS-DP-solutions-with-Picture-Clean-and-Concise-O(1)-Space
import collections

# first thought dfs (not pass)
def updateMatrix(mat):
    # dfs
    def dfs(pos: tuple, distance: int, visit):
        r, c = pos
        if r < 0 or c < 0 or r >= len(mat) or c >= len(mat[0]) or pos in visit:
            return float("inf")
        if mat[r][c] == 0:
            return distance
        visit.add(pos)
        res = float("inf")
        for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            res = min(res, dfs((r + y, c + x), distance + 1, visit))
        visit.remove(pos)
        return res

    res = []
    visit = set()
    for i in range(len(mat)):
        row = []
        for j in range(len(mat[0])):
            row.append(dfs((i, j), 0, visit))
        res.append(row)
    return res

# bfs
def updateMatrix2(mat):

    def bfs(pos: tuple):
        queue = collections.deque([(pos, 0)])
        visit = set()
        while queue:
            (r, c), d = queue.popleft()
            if not (r < 0 or c < 0 or r >= len(mat) or c >= len(mat[0]) or (r, c) in visit):
                visit.add((r, c))
                if mat[r][c] == 0:
                    return d
                for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    queue.append(((r + y, c + x), d + 1))

    res = []
    for i in range(len(mat)):
        row = []
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                row.append(0)
            else:
                row.append(bfs((i, j)))
        res.append(row)
    return res