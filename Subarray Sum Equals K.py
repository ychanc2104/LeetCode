# https://leetcode.com/problems/subarray-sum-equals-k/


# brute force, first thought, TC:O(n^2), SC:O(1)
def subarraySum(nums, k: int) -> int:
    res = 0
    n = len(nums)
    for i in range(n):
        count = 0
        for j in range(i, n):
            count += nums[j]
            if count == k:
                res += 1
    return res

# hash map, TC:O(n), SC:O(n)
def subarraySum2(nums, k: int) -> int:
    res = 0
    memo = {0: 1}  # first to meet sum as 0
    curSum = -k
    for i in range(len(nums)):
        print(memo, res, i, curSum)
        curSum += nums[i]
        if curSum in memo:
            # there are additional memo[curSum] valid subarray between 0 and i
            res += memo.get(curSum, 0)
        memo[curSum + k] = memo.get(curSum + k, 0) + 1
    return res