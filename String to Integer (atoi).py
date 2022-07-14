# https://leetcode.com/problems/string-to-integer-atoi/
# https://leetcode.com/problems/string-to-integer-atoi/discuss/798380/Fast-and-simpler-DFA-approach-(Python-3)

# Deterministic finite automaton, state machine, TC:O(n), SC:O(1)
def myAtoi(s: str) -> int:
    if not s:
        return 0
    state = 0
    sign = 1
    res = ''
    digit = set([str(i) for i in range(10)])
    for l in s:
        if state == 0:
            # init state
            if l == ' ':
                continue
            elif l == '-' or l == '+':
                state = 1
                sign = -1 if l == '-' else 1
            elif l in digit:
                res += l
                state = 2
            else:
                return 0
        elif state == 1:
            # +- state
            if l in digit:
                res += l
                state = 2
            else:
                return 0
        elif state == 2:
            # digit state
            if l in digit:
                res += l
            else:
                break
    res = '0' if not res else res
    res = min(int(res), 2 ** 31 - 1) if sign == 1 else max(-int(res), -2 ** 31)
    return res
