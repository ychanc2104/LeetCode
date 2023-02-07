# https://leetcode.com/problems/word-break/
# https://leetcode.com/problems/word-break/discuss/1455100/Python-3-solutions%3A-Top-down-DP-Bottom-up-DP-then-Optimised-with-Trie-Clean-and-Concise

import functools

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


#dp, TC:O(NMK + N^2), SC:O(N)
def wordBreak4(s: str, wordDict) -> bool:
    n = len(s)
    dp = [False] * (n+1)
    dp[0] = True
    # TC:O(NMK), N is length of s
    for i in range(1,n+1):
        s_sub = s[:i] # N
        # TC:O(MK) M is len(wordDict), K is word length
        for word in wordDict:
            m = len(word)
            if s_sub == word or (dp[i - m] and s_sub[i - m:] == word):  # prefix + suffix
                dp[i] = True
                break
    return dp[-1]

# top-down dp, TC:O(NM(N+K)), SC:O(NM)
def wordBreak5(s: str, wordDict) -> bool:
    wordDict_set = set(wordDict)
    @functools.lru_cache(None)
    def helper(s):
        if s in wordDict_set:
            return True
        for word in wordDict:
            if s.startswith(word) and helper(s[len(word):]):
                return True
        return False
    return helper(s)