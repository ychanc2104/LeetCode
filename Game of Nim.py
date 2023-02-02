# https://leetcode.com/problems/game-of-nim/description/
# https://leetcode.com/problems/game-of-nim/solutions/1318191/python-3-memoization-with-sorted-tuple/
# https://leetcode.com/problems/game-of-nim/solutions/1294891/o-n-sprague-grundy-theorem/
# https://zh.m.wikipedia.org/zh-tw/%E5%B0%BC%E5%A7%86%E6%B8%B8%E6%88%8F

from functools import lru_cache

# dfs + backtracking + dp, TC:O(NlogN*C(N+M-1, N)*NM), m is stone value, NlogN for sorting, C(N+M-1, N) for choosing a set of r items from n types of items,
# SC:O(C(N+M-1, N))
def nimGame(piles: List[int]) -> bool:
    remaining = sum(piles)

    @lru_cache(None)
    def dfs(status, remaining):
        if remaining == 0:
            return False  # previous state win
        piles = list(status)

        for j in range(len(piles)):
            if piles[j] == 0:
                continue
            for num in range(1, piles[j] + 1):
                piles[j] -= num
                # sort to cache 0,1,2 and 2,0,1
                if not dfs(tuple(sorted(piles)), remaining - num):  # another player lose
                    return True
                piles[j] += num  # backtracking
        return False

    return dfs(tuple(sorted(piles)), remaining)

# TC:O(N), SC:O(1)
def nimGame2(piles: List[int]) -> bool:
    # do XOR sum(nim-sum), if res != 0 => 1st player wins
    res = 0
    for p in piles:
        res ^= p
    return res != 0