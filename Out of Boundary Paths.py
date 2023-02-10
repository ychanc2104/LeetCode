# https://leetcode.com/problems/out-of-boundary-paths/

import functools

# top-down dp, TC:O(NMk), SC:O(NMk)
def findPaths(m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    @functools.lru_cache(None)
    def helper(r, c, move=0):
        if not 0 <= r < m or not 0 <= c < n:
            return 1
        if move >= maxMove:
            return 0
        res = 0
        for ro, co in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            res += helper(r + ro, c + co, move + 1)
        return res

    return helper(startRow, startColumn) % (10 ** 9 + 7)