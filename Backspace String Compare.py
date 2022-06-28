# https://leetcode.com/problems/backspace-string-compare/
# https://leetcode.com/problems/backspace-string-compare/discuss/135603/JavaC%2B%2BPython-O(N)-time-and-O(1)-space



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