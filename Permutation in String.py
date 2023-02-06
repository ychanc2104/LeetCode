# https://leetcode.com/problems/permutation-in-string/

import collections


# sliding window, TC:O(N), SC:O(1)
def checkInclusion(s1: str, s2: str) -> bool:
    # counter of string in window is the same
    counter = collections.Counter(s1)
    L = 0
    for char in s2:
        counter[char] -= 1
        while counter[char] < 0:
            counter[s2[L]] += 1
            L += 1
        if all(v == 0 for v in counter.values()):
            return True
    return False


# sliding window, optimized by matched, TC:O(N), SC:O(1)
def checkInclusion2(s1: str, s2: str) -> bool:
    # counter of string in window is the same
    counter = collections.Counter(s1)
    n = len(counter)
    matched = 0 # match in counter
    L = 0
    for char in s2:
        counter[char] -= 1
        if counter[char] == 0:
            matched += 1
        while counter[char] < 0:
            if counter[s2[L]] == 0:
                matched -= 1
            counter[s2[L]] += 1
            L += 1
        if matched == n:
            return True
    return False