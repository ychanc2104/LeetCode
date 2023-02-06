# https://leetcode.com/problems/largest-divisible-subset/description/


import collections

# first thought, dp, TC:O(N^2), SC:O(N^2)
def largestDivisibleSubset(nums: List[int]) -> List[int]:
    n = len(nums)
    dp = collections.defaultdict(set) # num: list, update gcd
    res = []
    nums.sort()
    for i in range(n):
        a = nums[i]
        dp[a].add(a)
        for j in range(i):
            b = nums[j] # smaller
            if a % b == 0:
                if len(dp[b]) + 1 > len(dp[a]):
                    dp[a] = dp[b] | {a}
        if len(dp[a]) > len(res):
            res = dp[a]
    return res


# concise dp, TC:O(N^2), SC:O(N^2)
def largestDivisibleSubset2(nums: List[int]) -> List[int]:
    n = len(nums)
    dp = {-1: set()} # num: set, initial value
    res = []
    for a in sorted(nums):
        dp[a] = max([dp[b] for b in dp.keys() if a % b == 0], key=len) | {a}
        if len(dp[a]) > len(res):
            res = dp[a]
    return res