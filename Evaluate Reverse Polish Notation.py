# https://leetcode.com/problems/evaluate-reverse-polish-notation/


# first thought, use stack

# TC: O(N), SC:O(N)
def evalRPN(tokens) -> int:
    stack = []
    operator = set(['+', '-', '*', '/'])
    for i in range(len(tokens)):
        token = tokens[i]
        if token not in operator:
            stack.append(token)
            # edge case for ['18'] only
            ans = int(token)
        else:
            y = int(stack.pop())
            x = int(stack.pop())
            if token == '+':
                ans = x + y
            elif token == '-':
                ans = x - y
            elif token == '*':
                ans = x * y
            elif token == '/':
                ans = int(x / y)
            stack.append(ans)
    return ans