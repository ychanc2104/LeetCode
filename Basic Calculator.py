# https://leetcode.com/problems/basic-calculator/
# https://leetcode.com/problems/basic-calculator/discuss/62424/Python-concise-solution-with-stack.
# https://leetcode.com/problems/basic-calculator/discuss/1456850/Python-Basic-Calculator-I-II-III-easy-solution-detailed-explanation
# https://leetcode.com/problems/basic-calculator/solutions/2017431/stop-hating-parsing-problems-and-start-having-fun/

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
            res *= stack.pop()
            res += stack.pop()
            num = 0
    return res + prev_sign * num


# correct for I, II and III, TC:O(N), SC:O(N)
def calculate2(s: str) -> int:
    # 1 - (2+3)
    presign = '+'
    stack = []
    curnum = 0
    for e in s+'+':
        if e in '0123456789':
            curnum = curnum*10 + int(e)
            continue
        elif e == '(':
            stack.append(presign)
            stack.append(e)
            presign = '+'
        elif e in '+-)':
            if presign == '+':
                stack.append(curnum)
            elif presign == '-':
                stack.append(-curnum)
            # add previous num to stack
            if e == ')':
                curnum = 0
                while stack[-1] != '(':
                    curnum += stack.pop()
                stack.pop() # pop out '('
                presign = stack.pop()
            else:
                presign = e
                curnum = 0
        # print(stack)
    return sum(stack)