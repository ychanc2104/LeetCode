# https://leetcode.com/problems/backspace-string-compare/
# https://leetcode.com/problems/backspace-string-compare/discuss/135603/JavaC%2B%2BPython-O(N)-time-and-O(1)-space
# https://leetcode.com/problems/backspace-string-compare/discuss/145786/Python-tm

from functools import reduce

# first thought, TC:O(n), SC:O(n)
def backspaceCompare(s: str, t: str) -> bool:
    def remove(s):
        res = ''
        skip = 0
        for l in s[::-1]:
            if l == '#':
                skip += 1
            elif skip > 0:
                skip -= 1
            else:
                res += l
        return res

    return remove(s) == remove(t)

# first thought, TC:O(n), SC:O(n)
def backspaceCompare2(s: str, t: str) -> bool:
    function = lambda res, l: res + l if l != '#' else res[:-1]
    return reduce(function, s, '') == reduce(function, t, '')

# use stack, TC:O(n), SC:O(n)
def backspaceCompare3(s: str, t: str) -> bool:
    def clean(s):
        stack = []
        s = list(s)
        for l in s:
            if stack and l == '#':
                stack.pop()
            elif l != '#':
                stack.append(l)
        return stack
    return clean(s) == clean(t)

# use two pointers, TC:O(n), SC:O(1)
def backspaceCompare4(s: str, t: str) -> bool:
    ## important to get character excluding #
    def get_char(seq, i):
        if i < 0:
            return '', i
        skip = 0
        ## get character of s and skip #
        while seq[i] == '#' or skip > 0:
            if seq[i] == '#':
                skip += 1
            else:
                skip -= 1
            i -= 1
            if i < 0:
                return '', i
        return seq[i], i - 1


    skip_s, skip_t = 0, 0
    i_s, i_t = len(s) - 1, len(t) - 1
    while i_s >= 0 or i_t >= 0:
        ## get character of s and skip #
        char_s, i_s = get_char(s, i_s)
        ## get character of s and skip #
        char_t, i_t = get_char(t, i_t)
        ## check
        if char_s != char_t:
            return False
    return True


s = "ab##"
t = "c#d#"

res1 = backspaceCompare(s, t)
res2 = backspaceCompare2(s, t)