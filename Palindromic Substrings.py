# https://leetcode.com/problems/palindromic-substrings/


## first thought, TC: O(n^3), O(n) for check and O(n^2) for iteration
def countSubstrings(s: str) -> int:
    n = len(s)
    res = n
    # O(n)
    for i in range(2, n + 1):
        # sub length
        # O(n)
        for j in range(n - i + 1):
            # O(n) to check
            s_sub = s[j:j + i]
            if s_sub == s_sub[::-1]:
                res += 1
    return res

## dp, TC: O(n^2), SC: O(n^2)
def countSubstrings2(s: str) -> int:
    n = len(s)
    # dp[i][j] => is s[i:j+1] a palindrome
    dp = [[False] * n for _ in range(n)]
    ans = 0
    # bottom-up
    for i in range(n-1,-1,-1):
        for j in range(i, n):
            dp[i][j] = (s[i]==s[j]) and (j-i<=1 or dp[i+1][j-1])
            if dp[i][j]:
                ans += 1
    print(dp)
    return ans

## expand at the center, TC: O(n^2)
def countSubstrings3(s: str) -> int:
    s = f"@{'#'.join(s)}$"
    # print(s)
    n = len(s)
    ans = 0
    for i in range(n):
        j = 0
        while i - j >= 0 and i + j < n:
            if s[i - j] == s[i + j]:
                if s[i - j] != "#" and s[i - j] != "@" and s[i - j] != "$":
                    # palindrome
                    ans += 1
            else:
                break
            j += 1
    return ans


## dp, TC: O(n^2), SC: O(n^2)
def countSubstrings4(s: str) -> int:
    # dp[i][j]: is s[i:j+1] palindrome
    # xabax
    res = 0
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if i == j:
                dp[i][j] = True
            else:
                if s[i] == s[j]:
                    if i + 1 == j or dp[i + 1][j - 1]:  # two string
                        dp[i][j] = True
            if dp[i][j]:
                res += 1
    return res

s = "abbba"
res = countSubstrings(s)