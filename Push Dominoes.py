# https://leetcode.com/problems/push-dominoes/description/

import collections

# first thought, BFS, TC:O(N), SC:O(N)
def pushDominoes(dominoes: str) -> str:
    n = len(dominoes)
    res = list(dominoes)
    # bfs
    queue = collections.deque([])  # idx, dist
    dist = [0] * n  # -1 for L, 1 for R
    for i, l in enumerate(dominoes):
        if l in ['L', 'R']:
            queue.append((i, 0))
    while queue:
        idx, d = queue.popleft()
        if res[idx] == 'L' and idx > 0:
            if res[idx - 1] == '.':
                res[idx - 1] = 'L'
                dist[idx - 1] = d - 1
                queue.append((idx - 1, d - 1))
            elif res[idx - 1] == 'R' and dist[idx - 1] + (d - 1) == 0:
                res[idx - 1] = '.'
        elif res[idx] == 'R' and idx < n - 1:
            if res[idx + 1] == '.':
                res[idx + 1] = 'R'
                dist[idx + 1] = d + 1
                queue.append((idx + 1, d + 1))
            elif res[idx + 1] == 'L' and dist[idx + 1] + (d + 1) == 0:  # equal force
                res[idx - 1] = '.'  # change

    return ''.join(res)

# compute forces, TC:O(N), SC:O(N)
def pushDominoes2(dominoes: str) -> str:
    n = len(dominoes)
    force = [0] * n  # -1 for L and +1 for R
    f = 0
    for i in range(n):
        d = dominoes[i]
        if d == 'R':
            f = n
        elif d == 'L':
            f = 0
        else:
            f = max(0, f - 1)
        force[i] = f
    f = 0
    for i in range(n - 1, -1, -1):
        d = dominoes[i]
        if d == 'L':
            f = -n
        elif d == 'R':
            f = 0
        else:
            f = min(0, f + 1)
        force[i] += f
    res = []
    for f in force:
        if f == 0:
            res.append('.')
        elif f > 0:
            res.append('R')
        else:
            res.append('L')
    return ''.join(res)