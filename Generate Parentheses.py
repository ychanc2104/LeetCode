# https://leetcode.com/problems/generate-parentheses/
# https://en.wikipedia.org/wiki/Catalan_number
# https://leetcode.com/problems/generate-parentheses/discuss/10099/Time-complexity-to-generate-all-combinations-of-well-formed-parentheses.

# 2n positions and each position with 2 choices('(' or ')')
# Catalan number, Cn = 1,1,2,5,14,42,132,429... n = 0,1,2,3,4,5,6,7...

# backtracking, Catalan number, TC:O(4^n/sqrt(n)), SC:O(4^n/sqrt(n))
def generateParenthesis(n: int):
    res = []
    path = []

    def backtrack(left, right):
        if left + right >= 2 * n:
            res.append(''.join(path))
            return
        # left parentheses are not enough
        if left < n:
            path.append('(')
            backtrack(left + 1, right)
            path.pop()
        # add right parentheses
        if left > right:
            path.append(')')
            backtrack(left, right + 1)
            path.pop()

    backtrack(0, 0)
    return res

# Closure Number
def generateParenthesis2(n: int):
    if n == 0: return ['']
    ans = []
    for c in range(n):
        for left in generateParenthesis2(c):
            for right in generateParenthesis2(n - 1 - c):
                ans.append(f'({left}){right}')
    return ans

# iterative, TC:O(4^n/sqrt(n)), SC:O(4^n/sqrt(n))
def generateParenthesis3(n: int):
    res = []
    s = [("(", 1, 0)]
    while s:
        x, l, r = s.pop()
        if l - r < 0 or l > n or r > n:
            continue
        if l == n and r == n:
            res.append(x)
        s.append((x+"(", l+1, r))
        s.append((x+")", l, r+1))
    return res