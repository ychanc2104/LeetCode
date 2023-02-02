# https://leetcode.com/problems/maximum-subarray-sum-after-one-operation/description/
# https://leetcode.com/problems/maximum-subarray-sum-after-one-operation/solutions/1050177/easiest-python-solution-o-n-time-o-1-space/


# two states dp, TC:O(N), SC:O(1)
def maxSumAfterOperation(nums: List[int]) -> int:
    res = nums[0] ** 2
    no_square = nums[0]  # max sum without operation
    square = nums[0] ** 2  # max sum with operation
    for i in range(1, len(nums)):
        no_square, square = max(nums[i], no_square + nums[i]), \
            max(nums[i] ** 2, no_square + nums[i] ** 2, square + nums[i])
        res = max(res, square)
    return res