# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/


import functools


# first thought, top-down dp, TC:O(NM), SC:(NM)
def minimumDeleteSum(s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)

    @functools.lru_cache(None)
    def helper(i, j):
        if i == n and j == m:
            return 0
        if i == n:
            return helper(i, j + 1) + ord(s2[j])
        if j == m:
            return helper(i + 1, j) + ord(s1[i])
        if s1[i] == s2[j]:
            return helper(i + 1, j + 1)

        return min(helper(i + 1, j) + ord(s1[i]), helper(i, j + 1) + ord(s2[j]))

    return helper(0, 0)


# 2d bottom-up dp, TC:O(NM), SC:O(NM)
def minimumDeleteSum2(s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n,-1,-1):
        for j in range(m,-1,-1):
            # build initial value
            if i == n and j == m:
                continue
            elif i == n:
                dp[i][j] = dp[i][j+1] + ord(s2[j])
                continue
            elif j == m:
                dp[i][j] = dp[i+1][j] + ord(s1[i])
                continue
            # build dp array
            if s1[i] == s2[j]:
                dp[i][j] = dp[i+1][j+1] # jump from previous
            else:
                # choose smaller
                dp[i][j] = min(dp[i+1][j] + ord(s1[i]), dp[i][j+1] + ord(s2[j]))
    return dp[0][0]


# 2d bottom-up dp, TC:O(NM), SC:O(NM)
def minimumDeleteSum3(s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            # build initial value
            if i == 0 and j == 0:
                continue
            elif i == 0:
                dp[i][j] = dp[i][j-1] + ord(s2[j-1])
                continue
            elif j == 0:
                dp[i][j] = dp[i-1][j] + ord(s1[i-1])
                continue
            # build dp array
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] # jump from previous
            else:
                # choose smaller
                dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))
    return dp[-1][-1]

# space optimized 1d bottom-up dp, TC:O(NM), SC:O(M)
def minimumDeleteSum4(s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)
    dp = [0] * (m+1)
    for i in range(n+1):
        dp_prev = dp.copy() # => dp[i-1]
        for j in range(m+1):
            # build initial value
            if i == 0 and j == 0:
                continue
            elif i == 0:
                dp[j] = dp[j-1] + ord(s2[j-1])
                continue
            elif j == 0:
                dp[j] = dp_prev[j] + ord(s1[i-1])
                continue
            # build dp array
            if s1[i-1] == s2[j-1]:
                dp[j] = dp_prev[j-1] # jump from previous
            else:
                # choose smaller
                dp[j] = min(dp_prev[j] + ord(s1[i-1]), dp[j-1] + ord(s2[j-1]))
    return dp[-1]