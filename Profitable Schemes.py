# https://leetcode.com/problems/profitable-schemes/description/

import functools

# top-down dp, TC:O(NMk), SC:O(NMk)
def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:

    @functools.lru_cache(None)
    def helper(i, n, minProfit):  # take from i to m
        if i == len(profit):
            return minProfit == 0
        res = helper(i + 1, n, minProfit)  # not choose i-th
        if n - group[i] >= 0:
            res += helper(i + 1, n - group[i], max(0, minProfit - profit[i]))

        return res % (10 ** 9 + 7)

    return helper(0, n, minProfit)
