# https://leetcode.com/problems/word-break/
# https://leetcode.com/problems/word-break/discuss/1455100/Python-3-solutions%3A-Top-down-DP-Bottom-up-DP-then-Optimised-with-Trie-Clean-and-Concise


# dp, O()
def wordBreak(s: str, wordDict) -> bool:
    # s: length N, wordDict: length M
    dp = [False] * len(s)
    # O(N)
    for i in range(len(s)):
        # from the end of the string
        seg = s[len(s) - 1 - i:len(s)]
        # O(M)
        for word in wordDict:
            if seg.startswith(word) and (dp[len(seg) - len(word) - 1] or len(seg) - len(word) == 0):
                dp[i] = True
            # no need to lookup further
            if dp[i]:
                break
    return dp[-1]