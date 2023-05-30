# https://leetcode.com/problems/minimum-cost-to-cut-a-stick/


import functools

# top-down dp, TC:O(N^3), SC:O(N^2)
def minCost(n: int, cuts: List[int]) -> int:
    # 7+4+2+3=16
    cuts = [0] + sorted(cuts) + [n]

    @functools.lru_cache(None)
    def helper(left, right):
        if right - left == 1:
            return 0
        res = float("inf")
        for mid in range(left + 1, right):
            res = min(res, helper(left, mid) + helper(mid, right))

        return res + cuts[right] - cuts[left]

    return helper(0, len(cuts) - 1)