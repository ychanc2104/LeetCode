# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/description/
# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/solutions/2852788/python3-dp-explained-o-n-2/


import collections

# bottom-up 2D dp, TC:O(N^2), SC:O(N^2)
def numberOfArithmeticSlices(nums: List[int]) -> int:
    # dp[i][d]: number of weak arithmetic(len >= 2) ending with pos i and diff is d
    # d[i][d] = sum all dp[j][d]+1 for j < i
    res = 0
    dp = [collections.defaultdict(int) for _ in range(len(nums))]
    for i in range(1, len(nums)):
        for j in range(i):  # sum all previous elements
            diff = nums[i] - nums[j]
            res += dp[j][diff]  # valid count to add nums[i]
            dp[i][diff] += dp[j][diff] + 1
    return res


# bottom-up 2D dp, TC:O(N^2), SC:O(N^2)
def numberOfArithmeticSlices2(nums: List[int]) -> int:
    # start with i and diff is d
    res = 0
    dp = [collections.defaultdict(int) for _ in range(len(nums))]
    for i in range(len(nums)-1, -1, -1):
        for j in range(i+1, len(nums)):
            diff = nums[j] - nums[i]
            res += dp[j][diff]
            dp[i][diff] += dp[j][diff] + 1
    return res

# top-down dp, TC:O(N^2), SC:O(N^2)
def numberOfArithmeticSlices3(nums: List[int]) -> int:
    # start with i and diff is d
    dp = {}
    def helper(i, d):
        if (i, d) in dp: return dp[(i, d)]
        res = 0
        for k in search[nums[i] + d]:
            if k > i:
                res += helper(k, d) + 1
        dp[(i, d)] = res
        return res

    search = collections.defaultdict(list)
    for i, num in enumerate(nums):
        search[num].append(i)

    res = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            res += helper(j, nums[j] - nums[i])
    return res