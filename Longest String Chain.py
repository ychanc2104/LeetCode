# https://leetcode.com/problems/longest-string-chain/description/
# https://leetcode.com/problems/longest-string-chain/solutions/2153007/c-python-simple-solution-w-explanation-dp/

# bottom-up dp, TC:O(NlogN + NL^2), SC:O(N + NL)
def longestStrChain(words: List[str]) -> int:
    dp = {}
    words.sort(key=len)  # TC:O(nlogn)
    res = 1
    for word in words:  # TC:O(n)
        dp[word] = 1
        for j in range(len(word)):  # TC:O(L)
            predecessor = word[:j] + word[j + 1:]  # TC:O(L)
            if predecessor in dp:
                dp[word] = max(dp[predecessor] + 1, dp[word])
                res = max(res, dp[word])
    return res


# top-down dp, TC:O(NL^2), SC:O(NL)
def longestStrChain(words: List[str]) -> int:
    dp = {}
    words_set = set(words)
    def dfs(word):
        if word not in words_set:
            return 0
        if word in dp:
            return dp[word]
        res = 1
        for i in range(len(word)):
            predecessor = word[:i] + word[i+1:]
            res = max(1 + dfs(predecessor), res)
        dp[word] = res
        return dp[word]
    return max(dfs(word) for word in words)