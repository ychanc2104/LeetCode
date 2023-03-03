# https://leetcode.com/problems/edit-distance/description/
# https://leetcode.com/problems/edit-distance/solutions/159295/python-solutions-and-intuition/

# bottom-up dp, TC:O(NM), SC:O(NM)
def minDistance(word1: str, word2: str) -> int:
    # dp[i][j]: min dist of word1[i:] and word2[j:]
    n, m = len(word1), len(word2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        dp[i][m] = n - i  # word2 is '' empty
    for j in range(m):
        dp[n][j] = m - j  # word1 is '' empty
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if word1[i] == word2[j]:
                dp[i][j] = dp[i + 1][j + 1]
            else:
                # compare with insert, delete and replace(dp[i+1][j+1])
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1]) + 1
    return dp[0][0]