# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/description/


# first thought, TC:O(NlogN), SC:O(N)
def maximumBags(capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
    diff = [c - r for c, r in zip(capacity, rocks)]
    diff.sort()
    res = 0
    for d in diff:
        if additionalRocks - d < 0:
            return res
        additionalRocks -= d
        res += 1
    return res