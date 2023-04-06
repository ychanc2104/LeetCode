# https://leetcode.com/problems/reducing-dishes/



# first thought, top-down dp, TC:O(N^2), SC:O(N^2)
def maxSatisfaction(satisfaction: List[int]) -> int:
    satisfaction.sort()

    @functools.lru_cache(None)
    def helper(i, mul=1):
        if i == len(satisfaction):
            return 0
        not_removed = mul * satisfaction[i] + helper(i + 1, mul + 1)
        removed = helper(i + 1, mul)
        return max(not_removed, removed)

    return helper(0)


# greedy, TC:O(NlogN) for sorting, SC:O(N) for sorting
def maxSatisfaction(satisfaction: List[int]) -> int:
    satisfaction.sort()
    # -9,-8,-1,0,5
    # make positive as far as possible
    n = len(satisfaction)
    suffix = 0
    res = 0
    for i in range(n - 1, -1, -1):
        suffix += satisfaction[i]
        if suffix <= 0: # do not add value < 0
            break
        res += suffix
    return res