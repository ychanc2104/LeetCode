# https://leetcode.com/problems/longest-valid-parentheses/
# https://leetcode.com/problems/longest-valid-parentheses/discuss/1139982/Python-short-dp-explained
# https://leetcode.com/problems/longest-valid-parentheses/solutions/1139982/python-short-dp-explained/


import functools

# first thought, use stack and two pass, TC:O(n), SC:O(n)
def longestValidParentheses(s: str) -> int:
    stack = []  # (string, index)
    for i, e in enumerate(s):
        if stack:
            if e == ')' and stack[-1][0] == '(':
                stack.pop()
            else:
                stack.append((e, i))
        else:
            stack.append((e, i))
    # print(stack)
    stack.append(('', len(s)))
    start = -1
    res = 0
    for e, end in stack:
        res = max(res, end - start - 1)
        start = end
    return res

# remove useless in stack, use stack and two pass, TC:O(n), SC:O(n)
def longestValidParentheses2(s: str) -> int:
    stack = [] # (string, index)
    res = 0
    for i,e in enumerate(s):
        if stack and s[stack[-1]]=='(' and e==')':
            stack.pop()
        else:
            stack.append(i)
    #print(stack)
    stack.append(len(s))
    start = -1
    res = 0
    for end in stack:
        res = max(res, end - start - 1)
        start = end
    return res


# use stack and one pass, TC:O(n), SC:O(n)
def longestValidParentheses3(s: str) -> int:
    stack = [-1] # (index)
    res = 0
    for i,e in enumerate(s):
        if stack[-1]!=-1 and s[stack[-1]]=='(' and e==')':
            stack.pop()
            # after finish a pair, update res
            res = max(res, i - stack[-1])
        else:
            stack.append(i)
    return res


# trick, scan from left to right and right to left, TC:O(n), SC:O(1)
def longestValidParentheses3(s: str) -> int:
    res = 0
    n = len(s)
    # left to right scan
    L, R = 0, 0
    for i in range(n):
        if s[i] == '(':
            L += 1
        else:
            R += 1
        if L == R:
            res = max(res, L + R)
        elif L <= R:
            # initialize
            L, R = 0, 0
    # right to left scan
    L, R = 0, 0
    for i in range(n-1, -1, -1):
        if s[i] == '(':
            L += 1
        else:
            R += 1
        if L == R:
            res = max(res, L + R)
        elif R <= L:
            # initialize
            L, R = 0, 0
    return res

# top-down dp, TC:O(N), SC:O(N)
def longestValidParentheses4(s: str) -> int:
    @functools.lru_cache(None)
    def helper(i): # longest res end at i (must include i)
        if i == -1 or s[i] == '(': # no anwser can be end with '('
            return 0
        l = helper(i-1)
        if i-l-1 >= 0 and s[i-l-1] == '(':
            return helper(i-1) + helper(i-1-l-1) + 2
        return 0
    if not s: return 0
    return max(helper(i) for i in range(len(s)))


# bottom-up dp, TC:O(N), SC:O(N)
def longestValidParentheses5(s: str) -> int:
    n = len(s)
    dp = [0] * n # dp[i]: longest res end and include index i
    for i in range(1, n):
        if s[i] == '(': continue
        l = dp[i-1] # i-l-2 i-l-1 l(length) i
        if i-1-l>=0 and s[i-1-l] == '(':
            dp[i] = dp[i-1] + dp[i-1-l-1] + 2
    return max(dp) if s else 0