# https://leetcode.com/problems/partition-equal-subset-sum/
# https://leetcode.com/problems/partition-equal-subset-sum/discuss/1624939/C%2B%2BPython-5-Simple-Solutions-w-Explanation-or-Optimization-from-Brute-Force-to-DP-to-Bitmask



from functools import lru_cache

# dfs, O(2^N), SC:O(N)
def canPartition(nums) -> bool:
    s = sum(nums)
    if s % 2 == 1:
        return False
    target = s // 2

    def dfs(pos, cum):
        if pos >= len(nums):
            return False
        if cum == target:
            return True
        elif cum > target:
            return False
            # pick pos
        # dfs(pos+1, cum+nums[pos])
        # not pick pos
        # dfs(pos+1, cum)
        return dfs(pos + 1, cum + nums[pos]) or dfs(pos + 1, cum)

    return dfs(0, 0)

# using cache, O(NM), SC:O(NM), M is sum(nums)//2
def canPartition2(nums) -> bool:
    s = sum(nums)
    if s%2 == 1:
        return False
    target = s//2
    @lru_cache(maxsize=None)
    def dfs(pos, cum):
        if pos>=len(nums):
            return False
        if cum == target:
            return True
        elif cum > target:
            return False
        # pick pos
        #dfs(pos+1, cum+nums[pos])
        # not pick pos
        #dfs(pos+1, cum)
        return dfs(pos+1, cum+nums[pos]) or dfs(pos+1, cum)
    # O(2^N), SC:O(N)
    return dfs(0, 0)

# bottom-up dp, O(NM), SC:O(NM), M is sum(nums)//2
def canPartition3(nums) -> bool:
    s = sum(nums)
    if s % 2 == 1:
        return False
    # dp[n], sum(nums)//2 = n is True
    # dp[0] must be True
    target = s // 2
    dp = [True] + [False] * target

    for num in nums:
        for i in range(target, num - 1, -1):
            # range [target, num], do not be smaller than num
            if i - num == 0 or dp[i - num]:
                dp[i] = True
                # print(dp)
    return dp[-1]

# top down dp
def canPartition4(nums) -> bool:
    s = sum(nums)
    if s & 1:
        return False
    target = s // 2
    dp = {}
    def helper(i, target):
        if target == 0:
            return True
        if target < 0 or i >= len(nums):
            return False
        if (i, target) in dp:
            return dp[(i, target)]
        dp[(i, target)] = helper(i + 1, target - nums[i]) or helper(i + 1, target)  # choose or not choose
        return dp[(i, target)]

    return helper(0, target)


# bottom up dp, TC:O(NM), SC:O(M)
def canPartition5(nums) -> bool:
    s = sum(nums)
    if s & 1:
        return False
    target = s//2
    # bottom-up
    dp = [True] + [False] * target
    for num in nums:
        for t in range(target, num-1, -1):
            dp[t] = dp[t] or dp[t-num]
    #print(dp)
    return dp[-1]

# bit, TC:O(N), SC:O(1)
def canPartition5(nums) -> bool:
    # := assign and use total
    if (total := sum(nums)) & 1:
        return False

    dp = 1 << (total >> 1)
    for n in nums:
        dp |= dp >> n
    return dp & 1