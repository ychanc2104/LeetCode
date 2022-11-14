# https://leetcode.com/problems/power-of-two/description/

# use rightmost bit, TC:O(1), SC:O(1)
def isPowerOfTwo(n: int) -> bool:
    return n == (n & -n) and n