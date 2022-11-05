# https://leetcode.com/problems/reverse-integer/

# not allow to use 64bit integers, TC:O(logx), SC:O(1)
def reverse(x: int) -> int:
    neg = False
    int32_max = 2 ** 31 - 1
    if x < 0:
        x *= -1
        neg = True
        int32_max += 1
    res = 0
    while x:
        if res > int32_max // 10:
            return 0
        res *= 10
        digit = x % 10
        if res > int32_max - digit:
            return 0
        res += digit
        x //= 10
    return res if not neg else -res