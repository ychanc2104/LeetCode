# https://leetcode.com/problems/maximum-subarray/
# https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts
# https://leetcode.com/problems/maximum-subarray/discuss/1595195/C%2B%2BPython-7-Simple-Solutions-w-Explanation-or-Brute-Force-%2B-DP-%2B-Kadane-%2B-Divide-and-Conquer
# Kadane's algorithm, https://en.wikipedia.org/wiki/Maximum_subarray_problem
"""
Kadane's algorithm
The thought follows a simple rule:
If the sum of a subarray is positive, it has possible to make the next value bigger, so we keep do it until it turn to negative.
If the sum is negative, it has no use to the next element, so we break.
it is a game of sum, not the elements.
"""

def maxSubArray(nums):
    temp = 0
    res = []
    for num in nums:
        temp += num
        if temp > 0:
            res.append(temp)
        else:
            temp = 0
    if res:
        return max(res)
    else:
        return max(nums)


def maxSubArray3(nums):
    res = [nums[0]]
    for num in nums[1:]:
        if num > 0:
            res.append(max(num, num + res[-1]))
        elif res[-1] > 0:
            res.append(num + res[-1])
        else:
            res.append(num)
    # print(res)
    return max(res)

def maxSubArray4(nums):
    res = [nums[0]]
    for num in nums[1:]:
        res.append(max(num, num + res[-1]))

    # print(res)
    return max(res)

def maxSubArray5(nums):
    for i in range(len(nums) - 1):
        if nums[i] > 0:
            nums[i + 1] += nums[i]
    return max(nums)

nums = [-2,1,-3,4,-1,2,1,-5,4]

s = maxSubArray(nums)