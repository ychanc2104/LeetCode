# https://leetcode.com/problems/optimal-partition-of-string/


# TC:O(N), SC:O(1)
def partitionString(s: str) -> int:
    res = 1
    seen = set()
    for c in s:
        if c in seen:
            seen = set()
            res += 1
        seen.add(c)
    return res
