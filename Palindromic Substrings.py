# https://leetcode.com/problems/palindromic-substrings/
#


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
            print(i,j)
            dp[i][j] = (s[i]==s[j]) and (j-i<=1 or dp[i+1][j-1])
            # or
            # if j-i<=1:
            #     dp[i][j] = True if s[i]==s[j] else False
            # else:
            #     if s[i]==s[j] and dp[i+1][j-1]:
            #         dp[i][j] = True
            #     else:
            #         dp[i][j] = False
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


# def countSubstrings4(S) -> int:
#     ans, n, i = 0, len(S), 0
#     while (i < n):
#         j, k = i - 1, i
#         while k < n - 1 and S[k] == S[k + 1]: k += 1
#         ans += (k - j) * (k - j + 1) // 2
#         i, k = k + 1, k + 1
#         while ~j and k < n and S[k] == S[j]:
#             j, k, ans = j - 1, k + 1, ans + 1
#     return ans

s = "abbba"
res = countSubstrings(s)