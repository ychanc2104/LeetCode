# https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/description/
# https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/solutions/1887010/java-c-python-top-down-dp-solution/

import functools

# top-down dp, TC:O(NM), M is sum(len(piles[i])), SC:O(Nk)
def maxValueOfCoins(piles: List[List[int]], k: int) -> int:
    n = len(piles)

    @functools.lru_cache(None)
    def helper(idx, k):  # choose from piles[:idx+1] with k coins
        if k == 0 or idx == n:
            return 0

        res = helper(idx + 1, k)  # not choose idx
        curSum = 0
        for i in range(min(len(piles[idx]), k)):
            curSum += piles[idx][i]
            res = max(res, helper(idx + 1, k - i - 1) + curSum)

        return res

    return helper(0, k)