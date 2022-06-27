# https://leetcode.com/problems/ransom-note/

import collections


# TC: O(m+2n) ~ O(m+n)
def canConstruct(ransomNote: str, magazine: str) -> bool:
    counter_r = collections.Counter(ransomNote)
    counter_m = collections.Counter(magazine)
    for key in counter_r:
        if counter_r[key] > counter_m[key]:
            return False
    return True


def canConstruct2(ransomNote: str, magazine: str) -> bool:
    return all([ransomNote.count(r) <= magazine.count(r) for r in set(ransomNote)])


## TC: O(m+n)
def canConstruct3(ransomNote: str, magazine: str) -> bool:
    # if collection < 0 => disappear key
    return not collections.Counter(ransomNote) - collections.Counter(magazine)