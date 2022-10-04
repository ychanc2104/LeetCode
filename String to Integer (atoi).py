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

def myAtoi2(s: str) -> int:
    # once encounter +-, must be going to get number, otherwise return res
    state = 0 # 0:to accept +- or exclude, 1:to get number
    tempSum = 0
    sign = 1
    for l in s:
        if l in '0123456789':
            state = 1
            if sign == 1 and tempSum > (2**31-1-int(l))//10:
                return 2**31-1
            elif sign == -1 and tempSum > (2**31-int(l))//10:
                return -2**31
            tempSum = tempSum * 10 + int(l)
        elif l in '+-':
            if state == 0:
                state = 1
                sign = 1 if l=='+' else -1
            else:
                return sign * tempSum
        elif l == ' ' and state==0: # initial state
            continue
        else:
            # break
            return sign * tempSum
    return sign * tempSum
