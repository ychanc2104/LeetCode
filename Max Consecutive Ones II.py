# https://leetcode.com/problems/max-consecutive-ones-ii/


# first thought, dp, TC:O(N), SC:O(1)
def findMaxConsecutiveOnes(nums: List[int]) -> int:
    res = 1
    f0 = -1
    f1 = 0
    for num in nums:
        if num:
            f1 += 1
        else:
            res = max(res, f0 + f1 + 1)
            f0 = f1
            f1 = 0
    return max(res, f0 + f1 + 1)