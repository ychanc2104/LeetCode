# https://leetcode.com/problems/valid-anagram/
from collections import Counter

import collections
def isAnagram(s: str, t: str) -> bool:
    return collections.Counter(s) == collections.Counter(t)

s = "anagram"
t = "nagaram"
res = isAnagram(s,t)