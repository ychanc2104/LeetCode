# https://leetcode.com/problems/house-robber-ii/
#

# dp, use helper house rob, TC: O(n), SC: O(n)
# key: decide to rob a0 => remains a2 ~ an-1,
# not rob a0 => a1 ~ an
def rob(nums) -> int:
    def helper(nums):
        dp = {}
        # bottom-up
        for i in range(len(nums) - 1, -1, -1):
            # 2, 1, 0
            # dp[2] = 2
            # dp[1] = max(dp[2], dp[3]+3) = 3
            # dp[0] = max(dp[1], dp[2]+2) = 4
            dp[i] = max(dp.get(i + 1, 0), nums[i] + dp.get(i + 2, 0))
        return dp[0]

    # edge cases
    if len(nums) <= 3:
        return max(nums)
    else:
        # choose nums[0] or do not choose
        return max(helper(nums[:-1]), helper(nums[1:]))