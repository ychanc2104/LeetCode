# https://leetcode.com/problems/scramble-string/


import collections, functools

# top-down dp, TC:O(N^4), N^2*N states and N for string slice, SC:O(N^3)
def isScramble(s1: str, s2: str) -> bool:
    @functools.lru_cache(None)
    def helper(s, start):
        n = len(s)
        if collections.Counter(s) != collections.Counter(s1[start: start + n]):
            return False
        if n == 1:
            return True

        for i in range(1, n):
            sL, sR = s[:i], s[i:]
            # no swap
            if helper(sL, start) and helper(sR, start + len(sL)):
                return True
            # swap
            if helper(sR, start) and helper(sL, start + len(sR)):
                return True
        return False

    return helper(s2, 0)
