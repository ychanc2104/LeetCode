# https://leetcode.com/problems/perfect-squares/description/

import collections

# first thought, dp, TC:O(n*sqrt(n)), SC:O(N)
def numSquares(n: int) -> int:
    # 6 => dp[1]+dp[5], dp[2]+dp[4], 2*dp[3]
    dp = [float("inf")] * (n + 1)  # first perfect
    for i in range(1, n + 1):
        for j in range(1, int(i ** 0.5) + 1):
            square = j ** 2
            if i - square == 0:
                dp[i] = 1
            else:
                dp[i] = min(dp[i], dp[square] + dp[i - square])
    return dp[-1]

# greedy + bfs, TC:O(n^(h/2)) tree_node * tree_height, SC:O(n^(h/2))
def numSquares2(n: int) -> int:
    options = [i**2 for i in range(int(n**0.5),0,-1)]
    # bfs to find the shortest path
    queue = collections.deque([(n, 0)])
    while queue:
        rem, step = queue.popleft()
        for node in options:
            if rem-node < 0: continue
            if rem-node == 0:
                return step + 1
            queue.append((rem-node, step+1))
