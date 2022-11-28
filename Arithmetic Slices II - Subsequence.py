# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/description/
# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/solutions/2852788/python3-dp-explained-o-n-2/


import collections

# 2D dp, TC:O(N^2), SC:O(N^2)
def numberOfArithmeticSlices(self, nums: List[int]) -> int:
    # dp[i][d]: number of weak arithmetic(len >= 2) ending with pos i and diff is d
    # d[i][d] = sum all dp[j][d]+1 for j < i
    res = 0
    dp = [collections.defaultdict(int) for i in range(len(nums))]
    for i in range(1, len(nums)):
        for j in range(i):  # sum all previous elements
            diff = nums[i] - nums[j]
            res += dp[j][diff]  # valid count to add nums[i]
            dp[i][diff] += dp[j][diff] + 1
    return res