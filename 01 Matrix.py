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


# bfs, TC:O(N*M), SC:O(N*M),start from zero-cells and mark 1 as -1, relation=> mat[i][j] = neighbor_cell + 1
def updateMatrix3(mat):
    queue = collections.deque([])
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                queue.append((i, j))
            else:
                # mark non-zero cells
                mat[i][j] = -1
    while queue:
        r, c = queue.popleft()
        # four directions
        for x, y in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nr, nc = r + y, c + x
            if nr < 0 or nc < 0 or nr >= len(mat) or nc >= len(mat[0]) or mat[nr][nc] != -1:
                continue
            mat[nr][nc] = mat[r][c] + 1
            queue.append((nr, nc))
    return mat

# 2D DP, TC:O(N*M), SC:O(1)
def updateMatrix4(mat):
    # top-left to bottom-right
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] > 0:
                top = mat[i - 1][j] if i - 1 >= 0 else float("inf")
                left = mat[i][j - 1] if j - 1 >= 0 else float("inf")
                mat[i][j] = min(top, left) + 1
    # bottom-right to top-left
    for i in range(len(mat) - 1, -1, -1):
        for j in range(len(mat[0]) - 1, -1, -1):
            if mat[i][j] > 0:
                bottom = mat[i + 1][j] if i + 1 < len(mat) else float("inf")
                right = mat[i][j + 1] if j + 1 < len(mat[0]) else float("inf")
                mat[i][j] = min(mat[i][j], bottom + 1, right + 1)
    return mat