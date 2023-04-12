# https://leetcode.com/problems/simplify-path/description/
# https://leetcode.com/problems/simplify-path/solutions/1847357/c-easy-stack-simple-explained-algorithm/


# stack, TC:O(N), SC:O(N)
def simplifyPath(path: str) -> str:
    stack = ['']
    path_list = path.split('/')
    for c in path_list:
        if c == '' or c == '.':
            continue
        if c == '..':
            if stack[-1] != '':
                stack.pop()
        else:
            stack.append(c)
    # print(stack)
    res = '/'.join(stack)
    return res if res else '/'