# https://leetcode.com/problems/product-of-array-except-self/
# https://leetcode.com/problems/product-of-array-except-self/discuss/1342916/3-Minute-Read-Mimicking-an-Interview
# https://leetcode.com/problems/product-of-array-except-self/discuss/1597994/C%2B%2BPython-4-Simple-Solutions-w-Explanation-or-Prefix-and-Suffix-product-O(1)-space-approach


# first thought, O(n)
def productExceptSelf(nums):
    res = []
    temp = 1
    count_zero = 0
    for num in nums:
        if num == 0:
            count_zero += 1
        else:
            temp *= num
    if count_zero > 1:
        return [0] * len(nums)
    elif count_zero == 1:
        return [0 if num != 0 else temp for num in nums]
    else:
        return [temp // num if num != 0 else temp for num in nums]


## use prefix and suffix
def productExceptSelf2(nums):
    ans, suf, pre = [1]*len(nums), 1, 1
    for i in range(len(nums)):
        ans[i] *= pre               # prefix product from one end
        pre *= nums[i]
        ans[-1-i] *= suf            # suffix product from other end
        suf *= nums[-1-i]
    return ans