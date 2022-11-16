# https://leetcode.com/problems/guess-number-higher-or-lower/description/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# binary search, TC:O(logN), SC:O(1)
def guessNumber(n: int) -> int:
    L, R = 1, n
    while L <= R:
        mid = (L + R) // 2
        if guess(mid) == -1:
            R = mid - 1
        elif guess(mid) == 1:
            L = mid + 1
        else:
            return mid