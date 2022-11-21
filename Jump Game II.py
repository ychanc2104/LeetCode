# https://leetcode.com/problems/jump-game-ii/description/

# first thought dp, TC:O(N^2), SC:O(N)
def jump(nums: List[int]) -> int:
    # dp[i]: min step to reach i
    # dp[0] = 0
    # 0,1,min(1,2)
    dp = [float("inf")] * len(nums)
    dp[0] = 0
    for i in range(1, len(nums)):
        for j in range(i):  # to reach i
            step = nums[j]
            if j + step >= i:
                dp[i] = min(dp[i], dp[j] + 1)
    return dp[-1]

# greedy, TC:O(N), SC:O(1)
def jump2(nums: List[int]) -> int:
    if len(nums) == 1: return 0
    i = 0
    reach = nums[0]
    count = 1
    while reach < len(nums)-1:
        for j in range(i+1, reach+1):
            if j + nums[j] > reach:
                reach = j + nums[j]
                i = j # jump to optimal position
        count += 1
    return count


# concise greedy, TC:O(N), SC:O(1)
def jump3(nums: List[int]) -> int:
    if len(nums) == 1: return 0
    reach = max_reach = nums[0]
    count = 1
    for i in range(1, len(nums)-1):
        max_reach = max(max_reach, i + nums[i]) # find max to reach before reach
        if i == reach: # next round
            reach = max_reach
            count += 1
    return count