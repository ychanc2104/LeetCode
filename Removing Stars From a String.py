# https://leetcode.com/problems/removing-stars-from-a-string/description/


# stack, TC:O(N), SC:O(N)
def removeStars(s: str) -> str:
    stack = []
    for c in s:
        if c == '*':
            stack.pop()
        else:
            stack.append(c)
    return ''.join(stack)