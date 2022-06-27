# https://leetcode.com/problems/longest-palindrome/
# https://leetcode.com/problems/longest-palindrome/discuss/89587/What-are-the-odds-(Python-and-C%2B%2B)

import collections


# first thought, TC:O(n), SC:O(n)
def longestPalindrome(s: str) -> int:
    # TC: O(n)
    counter = collections.Counter(s)
    res = 0
    for v in counter.values():
        if v % 2 == 0:
            res += v
        else:
            res += v - 1
    return min(res + 1, len(s)) if res % 2 == 0 else res


def longestPalindrome2(s: str) -> int:
    counter = collections.Counter(s)
    odd = sum([v&1 for v in counter.values()])
    ## +1 only when odd number existing (odd>0)
    return len(s) - odd + (odd>0)