# https://leetcode.com/problems/find-original-array-from-doubled-array/description/

import collections


# TC:O(NlogN), SC:O(N)
def findOriginalArray(changed: List[int]) -> List[int]:
    # if you can find its double => add into ori array
    ori = []
    n = len(changed)
    memo = collections.Counter(changed)
    changed.sort()
    for num in changed:
        if memo[num] == 0:
            continue
        if memo[2 * num] > 0:
            ori.append(num)
            memo[num] -= 1
            memo[2 * num] -= 1
        else:
            return []
    return ori if len(ori) == n / 2 else []