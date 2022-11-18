# https://leetcode.com/problems/ugly-number/

# first thought, recursive, TC:O(logN), SC:O(logN)
def isUgly( n: int) -> bool:
    if n == 1: return True
    if n < 1: return False
    if not n % 2:
        return isUgly(n // 2)
    elif not n % 3:
        return isUgly(n // 3)
    elif not n % 5:
        return isUgly(n // 5)


# TC:O(logN), SC:O(1)
def isUgly(n: int) -> bool:
    if n == 0: return False

    def divide_rolling(n, d):
        while n%d == 0:
            n //= d
        return n

    for d in [2,3,5]:
        n = divide_rolling(n, d)
    return n == 1