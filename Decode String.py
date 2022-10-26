# https://leetcode.com/problems/decode-string/
# https://leetcode.com/problems/decode-string/discuss/87662/Python-solution-using-stack


# use stack, TC:1+2+3+...+N => O(N^2), K is num in s, SC:O(L), L is size of output
def decodeString(self, s: str) -> str:
    curStr = ""
    stack = []
    multiplier = 0
    for e in s:
        # print(stack)
        if e == '[':
            # start to store multiplier and curStr and initialize them
            # TC: O(1) for appending a size one list
            stack.append(multiplier)
            stack.append(curStr)
            multiplier = 0
            curStr = ''
        elif ord('0') <= ord(e) <= ord('9'):
            multiplier = multiplier * 10 + int(e)
        elif ord('a') <= ord(e) <= ord('z'):
            curStr += e
        elif e == ']':
            preStr = stack.pop()
            num = stack.pop()
            # TC:O(K+J)
            curStr = preStr + curStr * num
    return curStr


def decodeString2(s: str) -> str:
    count_stack = []
    str_stack = ['']
    num_set = set('0123456789')
    count = 0
    curStr = ''
    for l in s:
        if l in num_set:
            count = count * 10 + int(l)
        elif l == '[': # put prevStr into stack
            count_stack.append(count)
            str_stack.append(curStr)
            count = 0
            curStr = ''
        elif l == ']': # count current str and pre count
            curStr = str_stack.pop() + count_stack.pop() * curStr
        else:
            curStr += l
    return curStr