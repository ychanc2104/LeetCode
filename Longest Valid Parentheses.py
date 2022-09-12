# https://leetcode.com/problems/longest-valid-parentheses/
# https://leetcode.com/problems/longest-valid-parentheses/discuss/1139982/Python-short-dp-explained

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
            res = max(res, i - stack[-1])
        else:
            stack.append(i)
    return res
