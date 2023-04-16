# https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/description/


# two counter, TC:O(N), SC:O(1)
def findTheLongestBalancedSubstring(s: str) -> int:
    res = 0
    L = 0
    n = len(s)
    while L < n:
        if s[L] == '1':
            L += 1
            continue
        cnt0, cnt1 = 0, 0
        # count 0's
        while L < n and s[L] == '0':
            L += 1
            cnt0 += 1
        # count 1's
        while L < n and s[L] == '1':
            L += 1
            cnt1 += 1
        res = max(res, 2 * min(cnt0, cnt1))

    return res
