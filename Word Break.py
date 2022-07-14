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

# dp, TC:O(M*N*K) M is len(wordDict), K is avg len of word in wordDict, SC:O(N)
def wordBreak2(s: str, wordDict) -> bool:
    # dp[i]: is s[len(s)-1-i:len(s)] in wordDict
    # from end of s, if one word in wordDict is started with segement
    dp = [False] * len(s)
    # O(N*N)
    for i in range(len(s)):
        # slice, O(N)
        seg = s[len(s) - 1 - i: len(s)]
        for word in wordDict:
            if dp[i]:
                break
            n = len(word)
            if word == seg:
                dp[i] = True
            elif seg[:n] == word:
                dp[i] = dp[i - n]
    # print(dp)
    return dp[-1]

# dp, TC:O(N^3), SC:O(N)
def wordBreak3(s: str, wordDict) -> bool:
    word_set = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[len(s)]