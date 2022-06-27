# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# TC: O(logN), SC: O(1)
def firstBadVersion(n: int) -> int:
    # 1,2,3,...,n
    L = 0
    R = n - 1
    while L <= R:
        mid = (L + R) >> 1
        if isBadVersion(mid):
            R = mid - 1
        else:
            L = mid + 1
    return L