# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/


# first thought, stack, TC:O(N), SC:O(N)
def minRemoveToMakeValid(s: str) -> str:
    stack = []
    for i, e in enumerate(s):
        if e == '(':
            stack.append(i)
        elif e == ')':
            if stack and s[stack[-1]] == '(':
                stack.pop()
            else:
                stack.append(i)
    res = []
    discard = set(stack)
    for i, e in enumerate(s):
        if i in discard:
            continue
        res.append(e)
    return ''.join(res)