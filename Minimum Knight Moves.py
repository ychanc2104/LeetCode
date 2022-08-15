# https://leetcode.com/problems/minimum-knight-moves/
# https://leetcode.com/problems/minimum-knight-moves/discuss/947138/Python-3-or-BFS-DFS-Math-or-Explanation

import collections

# BFS, first thought, TC:O(MN), M=x, N=y, SC:O(MN)
def minKnightMoves(x: int, y: int) -> int:
    # BFS
    # if x<1 or y<1
    queue = collections.deque([((0, 0), 0)])
    visit = set()
    while queue:
        (pos, step) = queue.pop(0)
        if pos == (x, y):
            return step
        # eight directions
        for dx, dy in ((1, 2), (-1, 2), (1, -2), (-1, -2)):
            for _ in range(2):
                dx, dy = dy, dx
                pos2 = (pos[0] + dx, pos[1] + dy)
                if pos2 in visit:
                    continue
                if pos2 == (x, y):
                    return step + 1
                visit.add(pos2)
                queue.append((pos2, step + 1))

# dfs + dp, start from (x,y) to (0,0) only take two directions, (-1,-2) and (-2,-1), TC:O(MN), M=x, N=y, SC:O(MN)
def minKnightMoves(x: int, y: int) -> int:
    dp = {}

    def dfs(x, y):
        if x + y == 0:
            # base case: (0, 0)
            return 0
        elif x + y == 2:
            # base case: (1, 1), (0, 2), (2, 0)
            return 2
        elif (x, y) in dp:
            return dp[(x, y)]
        else:
            dp[(x, y)] = min(dfs(abs(x - 1), abs(y - 2)), dfs(abs(x - 2), abs(y - 1))) + 1
            return dp[(x, y)]

    res = dfs(abs(x), abs(y))
    # print(res)
    return res