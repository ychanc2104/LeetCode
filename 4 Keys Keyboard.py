# https://leetcode.com/problems/4-keys-keyboard/

import functools

# 1D tp-down dp, TC:O(N), SC:O(N)
def maxA(n: int) -> int:
    # 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:9, (4)8:12, 9:16, 10:20
    # (9)11:27, 12:36, 13:45, 14:
    @functools.lru_cache(None)
    def helper(n):
        if n <= 6:
            return n
        return max(helper(n - 6) * 5, helper(n - 5) * 4, helper(n - 4) * 3, helper(n - 3) * 2)

    return helper(n)