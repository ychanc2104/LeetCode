# https://leetcode.com/problems/basic-calculator-iii/description/
# https://leetcode.com/problems/basic-calculator-iii/solutions/127881/python-o-n-solution-using-recursion/


# use stack, TC:O(N), SC:O(N)
def calculate(s: str) -> int:
    presign = '+'
    curnum = 0
    stack = []  # store ( and /*, parse ()
    for e in s + '+':
        if e in '0123456789':
            curnum = curnum * 10 + int(e)
        elif e == '(':
            stack.append(presign)
            stack.append(e)
            presign = '+'

        elif e in '+-*/)':
            if presign == '+':
                stack.append(curnum)
            elif presign == '-':
                stack.append(-curnum)
            elif presign == '*':
                stack.append(stack.pop() * curnum)
            elif presign == '/':
                stack.append(int(stack.pop() / curnum))  # prevent -3//2 = -2
            if e == ')':
                curnum = 0
                while stack[-1] != '(':
                    curnum += stack.pop()
                stack.pop()  # remove (
                presign = stack.pop()
            else:
                presign = e
                curnum = 0
        # print(stack)
    return sum(stack)