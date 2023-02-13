# https://leetcode.com/problems/target-sum/description/
# https://leetcode.com/problems/target-sum/solutions/455024/dp-is-easy-5-steps-to-think-through-dp-questions/
# https://leetcode.com/problems/target-sum/solutions/97439/java-python-easily-understood/

import functools, collections

# first thought, TC:O(2^N), SC:O(N)
def findTargetSumWays(nums: List[int], target: int) -> int:
    res = 0

    def helper(i, target):  # knapsack, TC:O(2^N)
        nonlocal res
        if i == len(nums):
            if target == 0:
                res += 1
            return
        num = nums[i]
        helper(i + 1, target + num)
        helper(i + 1, target - num)

    helper(0, target)
    return res

# top-down dp, TC:O(NM), M is sum(nums), SC:O(N)
def findTargetSumWays2(nums: List[int], target: int) -> int:
    @functools.lru_cache(None)
    def helper(i, target): # knapsack, TC:O(2^N)
        if i == len(nums):
            if target == 0:
                return 1
            return 0
        num = nums[i]
        positive = helper(i+1, target + num)
        negative = helper(i+1, target - num)
        return positive + negative

    return helper(0, target)


# bottom-up dp, TC:O(NM), M is sum(nums), SC:O(N)
def findTargetSumWays3(nums: List[int], target: int) -> int:
    dp = collections.defaultdict(int)
    dp[0] = 1
    for num in nums:
        dp_new = collections.defaultdict(int) # update all sum
        for k in dp:
            dp_new[k+num] += dp[k]
            dp_new[k-num] += dp[k]
        dp = dp_new
    return dp[target]