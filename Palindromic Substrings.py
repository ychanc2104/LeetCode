# https://leetcode.com/problems/palindromic-substrings/
#


## first thought, TC: O(n^2-2n) ~ O(n^2)
def countSubstrings(s: str) -> int:
    n = len(s)
    res = n
    for i in range(2, n + 1):
        # sub length
        for j in range(n - i + 1):
            s_sub = s[j:j + i]
            if s_sub == s_sub[::-1]:
                res += 1
    return res

s = "abbba"
res = countSubstrings(s)