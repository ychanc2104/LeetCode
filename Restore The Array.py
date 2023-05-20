# https://leetcode.com/problems/restore-the-array/description/

import functools


# top-down dp, TC:O(Nlogk), SC:O(N)
def numberOfArrays(s: str, k: int) -> int:
    @functools.lru_cache(None)
    def helper(i):
        if i == len(s):
            return 1
        res = 0
        for size in range(1, len(s) - i + 1):
            if s[i] == '0': break

            sub = s[i:i + size] # size max is logk
            if int(sub) > k: # logk length at most for each sub
                break
            res += helper(i + size)
        return res % (1000000007)

    return helper(0)

# bottom-up dp, TC:O(Nlogk), SC:O(N)
def numberOfArrays2(s: str, k: int) -> int:
    n = len(s)
    dp = [0] * (n+1) # dp[i]: ans of s[i:], dp[i] = dp[i+1] + dp[i+2] + ...+ dp[i+logk]
    dp[-1] = 1
    nk = len(str(k))
    for i in range(n-1,-1,-1):
        if s[i] == '0': continue
        for j in range(1, n-i+1):
            if (i+j<n and s[i+j] == '0'): continue
            if j > nk or int(s[i:i+j]) > k: break
            dp[i] += dp[i+j]
        dp[i] %= 1000000007
    return dp[0]