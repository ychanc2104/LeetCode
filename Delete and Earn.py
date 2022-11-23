# https://leetcode.com/problems/delete-and-earn/?envType=study-plan&id=dynamic-programming-i

import functools

# top-down dp, TC:O(N+M) M is max number in nums, SC:O(N+M)
def deleteAndEarn(nums: List[int]) -> int:
    memo = {}
    max_num = 0
    for num in nums:
        memo[num] = memo.get(num, 0) + num
        max_num = max(max_num, num)

    @functools.lru_cache(None)
    def helper(num):
        if num < 0 or num > max_num:
            return 0
        return max(helper(num + 1), helper(num + 2) + memo.get(num, 0))

    return helper(0)

# top-down dp, TC:O(N+M) M is max number in nums, SC:O(N+M)
def deleteAndEarn2(nums: List[int]) -> int:
    memo = {}
    max_num = 0
    for num in nums:
        memo[num] = memo.get(num, 0) + num
        max_num = max(max_num, num)
    dp = {}
    def helper(num):
        if num < 0 or num > max_num:
            return 0
        if num in dp:
            return dp[num]
        dp[num] = max(helper(num + 1), helper(num + 2) + memo.get(num, 0))
        return dp[num]

    return helper(0)


# bottom-up dp, TC:O(N+M) M is max number in nums, SC:O(N+M)
def deleteAndEarn3(nums: List[int]) -> int:
    memo = {}
    max_num = 0
    for num in nums:
        memo[num] = memo.get(num, 0) + num
        max_num = max(max_num, num)
    dp = {}
    for i in range(max_num, -1, -1):
        dp[i] = max(dp.get(i+1, 0), dp.get(i+2, 0) + memo.get(i, 0))
    return dp[0]

# space optimized bottom-up dp, TC:O(N+M) M is max number in nums, SC:O(N)
def deleteAndEarn4(nums: List[int]) -> int:
    memo = {}
    max_num = 0
    for num in nums:
        memo[num] = memo.get(num, 0) + num
        max_num = max(max_num, num)
    f0 = 0
    f1 = 0
    for i in range(max_num, -1, -1):
        f2 = max(f1, f0 + memo.get(i, 0))
        f0, f1 = f1, f2
    return f1