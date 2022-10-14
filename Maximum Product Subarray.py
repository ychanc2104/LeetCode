# https://leetcode.com/problems/maximum-product-subarray/
# https://leetcode.com/problems/maximum-product-subarray/discuss/847520/Thought-process-and-useful-strategy

## first thought, brute force, TC: O(n^2)
def maxProduct(nums) -> int:
    res = nums[0]
    n = len(nums)
    for i in range(n):
        sub = nums[i]
        res = max(res, sub)
        for j in range(i + 1, n):
            sub = sub * nums[j]
            res = max(res, sub)
    return res


# TC: O(n)
def maxProduct2(nums) -> int:
    minRes = maxRes = res = nums[0]
    for num in nums[1:]:
        if num < 0:
            # swap max and min, !!trick!!
            minRes, maxRes = maxRes, minRes
        # MIN(MAX) is num(itself) or contiguous array(num*MIN(MAX))
        minRes = min(num, num * minRes)
        maxRes = max(num, num * maxRes)
        res = max(res, maxRes)
    return res

# TC: O(n)
def maxProduct3(nums) -> int:
    minRes = maxRes = res = nums[0]
    for num in nums[1:]:
        # must be max or min
        maxRes, minRes = max(num, max(num * maxRes, num * minRes)), min(num, min(num * minRes, num * maxRes))
        res = max(res, maxRes)
    return res


# TC: O(n)
def maxProduct4(nums) -> int:
    res = nums[0]
    tempMax = nums[0] # store max
    tempMin = nums[0] # store min
    for i in range(1, len(nums)):
        temp = tempMax
        tempMax = max(nums[i], temp * nums[i], tempMin * nums[i])
        tempMin = min(nums[i], temp * nums[i], tempMin * nums[i])
        res = max(res, tempMax)
    return res