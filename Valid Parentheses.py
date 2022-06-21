
def isValid(s):
    stack = []
    check_dict = {'[': ']', '(': ')', '{': '}'}
    for e in s:
        if e in check_dict:
            stack.append(e)
        elif len(stack) != 0 and e == check_dict[stack[-1]]:
            stack.pop()
        else:
            return False
        print(f"stack is {''.join(stack)}")
    if len(stack)==0:
        return True
    else:
        return False

# O(n)
def isValid2(s):
    stack = []
    check_dict = {'[': ']', '(': ')', '{': '}'}
    for b in s:
        if b in check_dict:
            stack.append(b)
        # find pair of parentheses
        elif stack and b==check_dict[stack[-1]]:
            stack.pop()
        else: return False
    return True if not stack else False


s= '({})[]{}'

print(isValid(s))

# stack = []
# check_dict = {'[': ']', '(': ')', '{': '}'}
# for e in s:
#     if e in check_dict:
#         stack.append(e)
#     elif e == check_dict[stack[-1]] and len(stack) != 0:
#         stack.pop()
#     else:
#         result = False
#     print(f"stack is {''.join(stack)}")