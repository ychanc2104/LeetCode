# https://leetcode.com/problems/house-robber/
# https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.
# https://leetcode.com/problems/house-robber/discuss/55696/Python-solution-3-lines.

from functools import lru_cache

## first thought, brute force
def rob(nums) -> int:
    res = 0

    def dfs(pos, cum):
        nonlocal res
        # print(pos, cum, res)
        if pos >= len(nums):
            res = max(res, cum)
            # print('return', cum, res)
            return cum
        # two choices
        # update res only when pos>=len(nums)
        if pos < len(nums):
            dfs(pos + 2, cum + nums[pos])
        if pos + 1 < len(nums):
            dfs(pos + 3, cum + nums[pos + 1])
        # print('update', res)
        return cum + nums[pos]

    dfs(0, 0)
    return res

# simple recursive (timeout)
def rob2(nums) -> int:
    def helper(pos):
        if pos >= len(nums):
            return 0
        return max(nums[pos] + helper(pos + 2), helper(pos + 1))
    return helper(0)

# with cache, dp like
def rob2c(nums) -> int:
    @lru_cache(maxsize=None)
    def helper(i):
        if i>=len(nums):
            return 0
        return max(helper(i+1), nums[i] + helper(i+2))
    return helper(0)

## dp solution, top-down
def rob3(nums):
    dp = {}
    def helper(pos):
        if pos in dp:
            return dp[pos]
        if pos >= len(nums):
            return 0
        dp[pos] = max(nums[pos] + helper(pos + 2), helper(pos + 1))
        return dp[pos]
    return helper(0)


# dp, simple
def rob4(nums):
    # f(0) = nums[0], f(1) = max(num[0], nums[1]), f(2) = max(nums[2]+f(0), f(1))
    # f(n) = max(nums[n]+f(n-2), f(n-1)), for n > 0, f(n) = 0 for n < 0
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums)
    else:
        f0 = nums[0]
        f1 = max(nums[0], nums[1])
        for num in nums[2:]:
            f2 = max(num + f0, f1)
            f0 = f1
            f1 = f2
        return f2

# dp, simple
def rob5(nums):
    f0 = 0
    f1 = 0
    for num in nums:
        f2 = max(num+f0, f1)
        f0, f1 = f1, f2
    return f2

# dp
def rob6(nums):
    dp = {}
    # bottom-up
    for i in range(len(nums) - 1, -1, -1):
        # 2, 1, 0
        # dp[2] = 2
        # dp[1] = max(dp[2], dp[3]+3) = 3
        # dp[0] = max(dp[1], dp[2]+2) = 4
        dp[i] = max(dp.get(i + 1, 0), nums[i] + dp.get(i + 2, 0))
    return dp[0]

# dp, bottom-up
def rob7(nums):
    dp = [0] * (len(nums) + 2)
    for i in range(len(nums) - 1, -1, -1):
        dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
    # print(dp)
    return dp[0]



nums = [226,174,214,16,218,48,153,131,128,17,157,142,88,43,37,157,43,221,191,68,206,23,225,82,54,118,111,46,80,49,245,63,25,194,72,80,143,55,209,18,55]
nums = [1,2,3,4,5,6,7,8]
res = rob(nums)

res2 = rob2(nums)
