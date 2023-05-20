# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/description/


import functools

# top-down dp, TC:(N^2), SC:O(N^2)
def minInsertions(s: str) -> int:
    @functools.lru_cache(None)
    def helper(L, R):  # insert L or R
        if L > R:
            return 0

        if s[L] != s[R]:
            return min(helper(L + 1, R), helper(L, R - 1)) + 1
        return helper(L + 1, R - 1)

    return helper(0, len(s) - 1)


# bottom-up dp, TC:(N^2), SC:O(N^2)
def minInsertions2(s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)] # dp[i][j]: min from s[i:j+1]
    for i in range(n-1,-1,-1):
        for j in range(i+1, n):
            if s[i] != s[j]:
                dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
            else:
                dp[i][j] = dp[i+1][j-1]
    # print(dp)
    return dp[0][-1]


# space-optimized bottom-up dp, TC:(N^2), SC:O(N)
def minInsertions3(s: str) -> int:
    n = len(s)
    dp = [0] * n # dp[i][j]: min from s[i:j+1]
    for i in range(n-1,-1,-1):
        prev = 0
        for j in range(i+1, n):
            temp = dp[j]
            if s[i] != s[j]:
                dp[j] = min(dp[j], dp[j-1]) + 1
            else:
                dp[j] = prev
            prev = temp
    # print(dp)
    return dp[-1]