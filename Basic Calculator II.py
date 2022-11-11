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


# use stack, TC:O(N), SC:O(N)
def calculate3(s: str) -> int:
    # num => add to curNum
    # +,- => add sign*curNum to stack
    # *,/ => stack.pop()*,/curNum
    stack = []
    curNum = 0
    prevSign = '+'
    for l in s+'+':
        if l == ' ': continue
        if l in '0123456789':
            curNum = curNum * 10 + int(l)
            continue
        if prevSign in '+-':
            stack.append(curNum if prevSign == '+' else -curNum)
        elif prevSign in '*/':
            stack.append(stack.pop() * curNum if prevSign == '*' else int(stack.pop() / curNum))
        prevSign = l
        curNum = 0
    return sum(stack)

# space optimized, TC:O(N), SC:O(1)
def calculate4(s: str) -> int:
    curNum = 0
    prevNum = 0
    res = 0
    prevSign = '+'
    for l in s+'+':
        if l == ' ': continue
        if l in '0123456789':
            curNum = curNum * 10 + int(l)
            continue
        if prevSign in '+-':
            res += prevNum
            prevNum = curNum if prevSign == '+' else -curNum
        elif prevSign in '*/':
            prevNum = prevNum * curNum if prevSign == '*' else int(prevNum / curNum)
        prevSign = l
        curNum = 0
    return res + prevNum