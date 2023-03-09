# https://leetcode.com/problems/remove-k-digits/description/


def removeKdigits(self, num: str, k: int) -> str:
    stack = []
    for c in num:

        while k and stack and stack[-1] > c:
            stack.pop()
            k -= 1
        if not stack and c == '0':
            continue
        stack.append(c)
    while k and stack:
        stack.pop()
        k -= 1
    return ''.join(stack) if stack else '0'
