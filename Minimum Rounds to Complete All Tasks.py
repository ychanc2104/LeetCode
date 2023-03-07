# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/description/

import collections

# TC:O(N), SC:O(N)
def minimumRounds(tasks: List[int]) -> int:
    counter = collections.Counter(tasks)
    res = 0
    for v in counter.values():
        if v == 1:
            return -1
        elif v % 3 == 0:
            res += v // 3
        else:
            res += v // 3 + 1

    return res
