# https://leetcode.com/problems/stone-game-ii/


import functools


# top-down dp, TC:O(N^3), SC:O(N^2), N^2 states
def stoneGameII(piles: List[int]) -> int:
    @functools.lru_cache(None)
    def helper(i=0, M=1, role=1):
        if i >= len(piles):
            return 0
        res = 0 if role == 1 else float("inf")
        s = 0
        for x in range(1, 2 * M + 1):
            s += piles[i + x - 1] if i + x - 1 < len(piles) else 0
            if role == 1:  # alice, make bob min
                res = max(res, helper(i + x, max(x, M), -1) + s)
            else:  # bob, make alice min
                res = min(res, helper(i + x, max(x, M), 1))
        return res

    return helper(0)