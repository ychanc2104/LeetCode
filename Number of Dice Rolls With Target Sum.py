# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

import functools


# top-down dp, TC:O(NMk), SC:O(NM)
def numRollsToTarget(n: int, k: int, target: int) -> int:
    @functools.lru_cache(None)
    def helper(n, target):
        if n == 1:
            if target <= k:
                return 1
            return 0
        res = 0
        for i in range(1, k + 1):
            if target - i <= 0:
                continue
            res += helper(n - 1, target - i)
        return res % (10 ** 9 + 7)

    return helper(n, target)


# bottom-up dp, TC:O(NMk), SC:O(NM)
def numRollsToTarget2(n: int, k: int, target: int) -> int:
    dp = [{} for _ in range(n)]
    for m in range(1, k+1):
        dp[0][m] = 1
    for i in range(1, n):
        for j in dp[i-1]:
            for m in range(1, k+1):
                dp[i][j+m] = dp[i].get(j+m, 0) + dp[i-1][j]

    return dp[-1].get(target, 0) % (10**9 + 7)