# https://leetcode.com/problems/longest-palindromic-subsequence/description/
# https://leetcode.com/problems/longest-palindromic-subsequence/solutions/1468396/c-python-2-solutions-top-down-dp-bottom-up-dp-o-n-space-clean-concise/


import functools

# first thought, TLE
def longestPalindromeSubseq(s: str) -> int:
    @functools.lru_cache(None)
    def helper(s):
        res = 1
        for j in range(len(s)):  # pos
            sub = s[:j] + s[j + 1:]
            print(sub)
            if sub == sub[::-1]:
                return len(sub)
            res = max(res, helper(sub))
        return res

    if s == s[::-1]:
        return len(s)
    return helper(s)

# top-down dp, TC:O(N^2), SC:O(N^2) for cache
def longestPalindromeSubseq2(s: str) -> int:
    # dp[i][j]: s[i:j+1] is palindrome or not

    @functools.lru_cache(None)
    def helper(L, R):
        if L > R:  # empty string
            return 0
        if L == R:
            return 1

        if s[L] == s[R]:
            return 2 + helper(L + 1, R - 1)
        return max(helper(L + 1, R), helper(L, R - 1))

    return helper(0, len(s) - 1)

# bottom-up dp, TC:O(N^2), SC:O(N^2) for cache
def longestPalindromeSubseq3(s: str) -> int:
    # dp[i][j]: longest Palindromic Subsequence in s[i:j+1]
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if i == j:
                dp[i][j] = 1
            elif i < j:
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
    # print(dp)
    return dp[0][-1]

s = "euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"
res = longestPalindromeSubseq(s)