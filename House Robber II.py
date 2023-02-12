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


# top-down dp, TC: O(n), SC: O(n)
def rob2(nums) -> int:
    # 1:n+1 and 0:n
    def rob1(arr):
        @functools.lru_cache(None)
        def helper(i):
            if i >= len(arr):
                return 0
            return max(helper(i+1), helper(i+2) + arr[i])
        return helper(0)
    n = len(nums)
    return max(rob1(nums[:-1]), rob1(nums[1:]), nums[0])