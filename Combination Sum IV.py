# https://leetcode.com/problems/combination-sum-iv/

import collections

# first thought, backtracking, TC:O(N^target)
def combinationSum4(nums: list, target: int) -> int:
    res = [0]
    curSum = [0]

    # TC:O(N^target)
    def backtrack(pos=0):
        if curSum[0] == target:
            res[0] += 1
            return
        elif curSum[0] > target or pos >= target:
            return

        for i in range(len(nums)):
            curSum[0] += nums[i]
            backtrack(pos + 1)
            curSum[0] -= nums[i]

    backtrack()
    return res[0]

# bottom-up dp, TC:O(N*T), SC:O(T), T is target
def combinationSum42(nums: list, target: int) -> int:
    dp = collections.defaultdict(int)
    dp[0] = 1
    # bottom-up
    for i in range(1, target+1):
        for num in nums:
            if i-num < 0:
                continue
            dp[i] += dp[i-num]
        #print(dp[i])
    return dp[target]