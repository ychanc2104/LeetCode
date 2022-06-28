# https://leetcode.com/problems/roman-to-integer/


# first thought, TC:O(n), SC:O(1)
def romanToInt(s: str) -> int:
    # special: IV, IX, XL, XC, CD, CM
    res = 0
    memo = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    pre = ''
    for r in s[::-1]:
        if r == 'I' and pre in ['V', 'X']:
            res -= memo[r]
        elif r == 'X' and pre in ['L', 'C']:
            res -= memo[r]
        elif r == 'C' and pre in ['D', 'M']:
            res -= memo[r]
        else:
            res += memo[r]
        pre = r
    return res

# check if previous > current
def romanToInt2(s: str) -> int:
    res = 0
    memo = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev = s[-1]
    for r in s[::-1]:
        res += memo[r] if memo[r] >= memo[prev] else -memo[r]
        prev = r
    return res