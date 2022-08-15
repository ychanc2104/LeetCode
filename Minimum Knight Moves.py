# https://leetcode.com/problems/minimum-knight-moves/


import collections

# BFS, first thought
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