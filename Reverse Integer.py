# https://leetcode.com/problems/reverse-integer/

# first thought, not required for not allow to store 64-bit integers, TC:O(logx), SC:O(1)
def reverse(x: int) -> int:
    sign = 1
    if x < 0:
        x = -x
        sign = -1
    res = 0
    while x:
        # 123 => (x,res)=(123,0),(12,3),(1,32),(0,321)
        res = res * 10 + x % 10
        x = x // 10
    res *= sign
    return res if -2 ** 31 <= res <= 2 ** 31 - 1 else 0

# not allow to use 64bit integers, TC:O(logx), SC:O(1)
def reverse2(x: int) -> int:

    sign = 1
    int32_max = 2 ** 31 - 1
    if x < 0:
        x = -x
        sign = -1
        int32_max += 1
    res = 0
    while x:
        # 123 => (x,res)=(123,0),(12,3),(1,32),(0,321)
        if int32_max // 10 < res // 10:
            return 0
        res *= 10
        digit = x % 10
        if int32_max - digit < res:
            return 0
        res += digit
        x = x // 10
    res *= sign
    return res