# https://leetcode.com/problems/minimum-score-by-changing-two-elements/description/


# compare three cases, TC:O(NlogN), SC:O(N) for sorting
def minimizeSum(nums: List[int]) -> int:
    n = len(nums)
    # 9,27,33,59,81
    # 8,28,42,58,75
    nums.sort()
    return min(nums[-1] - nums[2], nums[-3] - nums[0], nums[-2] - nums[1])