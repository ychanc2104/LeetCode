# https://leetcode.com/problems/unique-number-of-occurrences/description/

import collections

# first thought, TC:O(N), SC:O(N)
def uniqueOccurrences(arr: List[int]) -> bool:
    counter = collections.Counter(arr)
    seen = set()
    for v in counter.values():
        if v in seen:
            return False
        seen.add(v)
    return True

# one-liner, TC:O(N), SC:O(N)
def uniqueOccurrences2(arr: List[int]) -> bool:
    return len(set(collections.Counter(arr).values())) == len(set(arr))