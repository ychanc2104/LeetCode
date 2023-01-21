# https://leetcode.com/problems/shortest-palindrome/description/
# https://leetcode.com/problems/shortest-palindrome/solutions/60099/ac-in-288-ms-simple-brute-force/
# https://leetcode.com/problems/shortest-palindrome/solutions/60113/clean-kmp-solution-with-super-detailed-explanation/


# brute force, TC:O(N^2), SC:O(N)
def shortestPalindrome(s: str) -> str:
    rev = s[::-1]
    for i in range(len(s)):  # i=0 originally is a palindrome
        sub = rev[:i]
        if (sub + s).startswith(rev): # abcd, dcba (d+abcd).startswith(dcba)
            return sub + s
    return rev + s  # edge case: s=""

# brute force, TC:O(N^2), SC:O(N)
def shortestPalindrome2(s: str) -> str:
    rev_s = s[::-1]
    for i in range(len(s)):
        if s.startswith(rev_s[i:]): # add rev_s[:i] in front of s
            return rev_s[:i] + s
    return rev_s + s

# KMP, TC:O(2N)=O(N), SC:O(N)
def shortestPalindrome3(s: str) -> str:
    """
    ex: s = c a t a c b

    c a t a c b # b c a t a c

    0 0 0 0 1 0 0 0 1 2 3 4 5

    """
    n = len(s)
    if n < 2:
        return s # 0 or 1 char
    rev_s = s[::-1]
    l = s + "#" + rev_s #
    table = [0] * len(l) # need table[-1] to find how many chars in rev_s are same with s
    for i in range(1, len(l)):
        idx = table[i - 1]
        while idx > 0 and l[i] != l[idx]:
            idx = table[idx-1] # match fail, go to
        table[i] = idx + (l[i] == l[idx])
    return rev_s[:n - table[-1]] + s