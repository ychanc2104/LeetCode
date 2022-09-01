# https://leetcode.com/problems/basic-calculator-ii/
# https://leetcode.com/problems/basic-calculator-ii/discuss/63076/Python-short-solution-with-stack.


# use stack, TC:O(N), SC:O(N)
def calculate(s: str) -> int:
    stack = []
    prev_sign = '+'
    curr_num = ''
    num_set = set([str(i) for i in range(10)])
    for i, e in enumerate(s):
        if e in num_set:
            curr_num += e
        if e in '+-*/' or i == len(s) - 1:
            if prev_sign == '+':
                stack.append(int(curr_num))
            elif prev_sign == '-':
                stack.append(-int(curr_num))
            elif prev_sign == '*':
                stack.append(stack.pop() * int(curr_num))
            else:
                stack.append(int(stack.pop() / int(curr_num)))
            curr_num = ''
            prev_sign = e
    return sum(stack)

# space optimized, TC:O(N), SC:O(1)
def calculate2(s: str) -> int:
    prev_sign = '+'
    prev_num = 0
    curr_num = ''
    res = 0
    num_set = set([str(i) for i in range(10)])
    for i, e in enumerate(s):
        if e in num_set:
            curr_num += e

        if e in '+-*/' or i == len(s) - 1:
            if prev_sign == '+':
                res += prev_num
                prev_num = int(curr_num)
            elif prev_sign == '-':
                res += prev_num
                prev_num = -int(curr_num)

            elif prev_sign == '*':
                prev_num = prev_num * int(curr_num)
            else:
                prev_num = int(prev_num / int(curr_num))
            curr_num = ''
            prev_sign = e
    return res + prev_num