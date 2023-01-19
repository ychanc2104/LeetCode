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


# use two stacks, TC:O(N), SC:O(N)
def calculate2(s: str) -> int:
    equations = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    def evaluate():
        a, b = nums.pop(), nums.pop()
        num = equations[opts.pop()](b, a)
        nums.append(int(num))

    curnum = 0
    nums = [] # store confirmed value
    opts = []
    for e in s:
        if e in '0123456789':
            curnum = curnum*10 + int(e)
        elif e == '(':
            opts.append(e)
        elif e in '+-': # can process all
            nums.append(curnum)
            curnum = 0
            while opts and opts[-1] in '+-*/':
                evaluate()
            opts.append(e)
        elif e in '*/':
            nums.append(curnum)
            curnum = 0
            while opts and opts[-1] in '*/': # if opts and opts[-1] in '*/':
                evaluate()
            opts.append(e)
        elif e == ')':
            nums.append(curnum)
            while opts[-1] != '(':
                evaluate()
            curnum = nums.pop()
            opts.pop() # remove (
    # print(curnum, nums, opts)
    nums.append(curnum)
    while opts:
        evaluate()
    return nums[0]