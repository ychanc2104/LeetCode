# https://leetcode.com/problems/add-binary/


# first thought, TC:O(n), SC:O(n)
def addBinary(a: str, b: str) -> str:
    if len(a) > len(b):
        b = '0' * (len(a) - len(b)) + b
    elif len(b) > len(a):
        a = '0' * (len(b) - len(a)) + a
    res = ''
    carry = False
    for i in range(len(a) - 1, -1, -1):
        if a[i] == b[i] == '1':
            if carry:
                res = '1' + res
            else:
                res = '0' + res
            carry = True
        elif a[i] == b[i] == '0':
            if carry:
                res = '1' + res
                carry = False
            else:
                res = '0' + res
        else:
            if carry:
                res = '0' + res
            else:
                res = '1' + res
    if carry:
        res = '1' + res
    return res

# first thought, TC:O(n), SC:O(n)
def addBinary2(a: str, b: str) -> str:
    a = list(a)
    b = list(b)
    carry = 0
    res = ''
    while a or b or carry:
        # remove last
        if a:
            carry += int(a.pop())
        if b:
            carry += int(b.pop())
        res += '1' if carry%2==1 else '0'
        carry //= 2
    return res[::-1]