# https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/description/

import functools


# top-down dp, TC:O(N^2), SC:O(N)
def twoEggDrop(n: int) -> int:
    # f(2) = 2, f(3) = at 2, , f(4)=min(4, 4) = 3
    @functools.lru_cache(None)
    def helper(i):
        if i == 1:
            return 1
        res = float('inf')
        for j in range(1, i):  # at j floor
            broken = j - 1  # 0~j-1, j-1 trial
            not_broken = helper(i - j)  # j~i=> 0~i-j, helper(i-j)
            res = min(res, max(broken, not_broken) + 1)
        return res

    return helper(n)


# bottom-up dp, TC:O(N^2), SC:O(N)
def twoEggDrop2(n: int) -> int:
    # f(1) = 1, f(2) = 2, f(3) = at 2, , f(4)=min(4, 4) = 3
    dp = [float('inf')] * (n+1)
    dp[1] = 1
    for i in range(1, n+1):
        for j in range(1, i): # partition
            dp[i] = min(dp[i], max(j-1, dp[i-j]) + 1)
    return dp[n]


# pattern, TC:O(N), SC:O(1)
def twoEggDrop(n: int) -> int:
    # (n)   100,99,98,97,94,90,85
    # (gap)    1,2,3,4,5,6,...
    gap = 1
    while n > 0:
        n -= gap
        gap += 1
    return gap-1