# https://leetcode.com/problems/basic-calculator/
# https://leetcode.com/problems/basic-calculator/discuss/62424/Python-concise-solution-with-stack.
# https://leetcode.com/problems/basic-calculator/discuss/1456850/Python-Basic-Calculator-I-II-III-easy-solution-detailed-explanation

# use stack, TC:O(n), SC:O(n)
def calculate(s: str) -> int:
    # 1-3-(1-(2+3))+4
    stack = []  # store sign in to stack if encounter '('
    prev_sign = 1
    num = 0
    res = 0
    for e in s:
        if e.isdigit():
            num = num * 10 + int(e)
        elif e in '+-':
            res += prev_sign * num
            prev_sign = 1 if e == '+' else -1
            num = 0
        elif e == '(':
            # store previous res and sign
            stack.append(res)
            stack.append(prev_sign)
            res = 0
            prev_sign = 1
        elif e == ')':
            res += prev_sign * num
            res = stack.pop() * res
            res += stack.pop()
            num = 0
    return res + prev_sign * num

