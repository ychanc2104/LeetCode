# https://leetcode.com/problems/longest-common-subsequence/

import functools

# with hint, TC: O(nm)
# 1. Try dynamic programming. DP[i][j] represents the longest common subsequence of text1[0 ... i] & text2[0 ... j].
# 2. DP[i][j] = DP[i - 1][j - 1] + 1 , if text1[i] == text2[j] DP[i][j] = max(DP[i - 1][j], DP[i][j - 1]) , otherwise
def longestCommonSubsequence(text1: str, text2: str) -> int:
    dp = [[0 for i in text1] for j in text2]
    res = 0
    for i in range(len(text2)):
        for j in range(len(text1)):
            if text2[i] == text1[j]:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            res = max(res, dp[i][j])
    # print(dp)
    return res

# refine
def longestCommonSubsequence2(text1: str, text2: str) -> int:
    n = len(text1)
    m = len(text2)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text2[j - 1] == text1[i - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    # print(dp)
    return dp[n][m]


# top-down dp, TC: O(nm), SC:O(nm)
def longestCommonSubsequence3(text1: str, text2: str) -> int:
    n, m = len(text1), len(text2)

    @functools.lru_cache(None)
    def helper(i, j):
        if i == n or j == m:
            return 0

        if text1[i] == text2[j]:
            return 1 + helper(i + 1, j + 1)
        return max(helper(i + 1, j), helper(i, j + 1))

    return helper(0, 0)