# https://leetcode.com/problems/snakes-and-ladders/description/

import collections

# first thought, BFS, TC:O(N^2), SC:O(N^2)
def snakesAndLadders(board: List[List[int]]) -> int:
    # 1 => [2,7] do BFS
    def evaluate(i, j):
        if i % 2 == 0:  # even
            return i * n + j + 1
        return i * n + (n - j)

    def evaluate_p(v):
        i = (v - 1) // n
        j = (v - 1) % n if i % 2 == 0 else (i + 1) * n - v
        return (i, j)

    n = len(board)
    board = board[::-1]
    queue = collections.deque([((0, 0), 0)])  # r,c,step
    board[0][0] = 0
    dest = n ** 2
    while queue:
        (r, c), step = queue.popleft()
        val = evaluate(r, c)
        if val == dest:
            return step
        for v in range(val + 1, min(dest + 1, val + 7)):
            rn, cn = evaluate_p(v)
            cell = board[rn][cn]
            if cell == 0: continue
            board[rn][cn] = 0  # mark visited
            if cell == -1:
                queue.append(((rn, cn), step + 1))
                continue
            queue.append((evaluate_p(cell), step + 1))
    return -1


# BFS on value, TC:O(N^2), SC:O(N^2)
def snakesAndLadders2(board: List[List[int]]) -> int:
    # 1 => [2,7] do BFS
    n = len(board)
    queue = collections.deque([(1, 0)]) # val,step
    board[n-1][0] = 0
    while queue:
        val, step = queue.popleft()
        if val == n**2:
            return step
        for v in range(val+1, min(n**2+1, val+7)):
            # rn, cn = evaluate_p(v)
            rn, cn = (v-1)//n, (v-1)%n # 10 => 1,3 | 15 => 2,2 | 16 => 2,3
            rn, cn = ~rn, cn if not rn%2 else ~cn # from its head or its end
            cell = board[rn][cn]
            if cell == 0: continue
            board[rn][cn] = 0 # mark visited
            if cell == -1:
                queue.append((v, step + 1))
                continue
            queue.append((cell, step + 1))
    return -1