# https://leetcode.com/problems/power-of-two/description/

# use rightmost bit, TC:O(1), SC:O(1)
def isPowerOfTwo(n: int) -> bool:
    return n == (n & -n) and n

# logN
def isPowerOfTwo2(n: int) -> bool:
    if n == 0: return False
    elif n == 1: return True
    elif n % 2: return False
    return isPowerOfTwo2(n/2)

# logN
def isPowerOfTwo3(n: int) -> bool:
    if n == 1: return True
    elif n < 1: return False
    return isPowerOfTwo3(n/2)