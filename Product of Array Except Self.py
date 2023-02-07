# https://leetcode.com/problems/product-of-array-except-self/
# https://leetcode.com/problems/product-of-array-except-self/discuss/1342916/3-Minute-Read-Mimicking-an-Interview
# https://leetcode.com/problems/product-of-array-except-self/discuss/1597994/C%2B%2BPython-4-Simple-Solutions-w-Explanation-or-Prefix-and-Suffix-product-O(1)-space-approach


# 1d dp, TC:O(n), SC:O(n)
def productExceptSelf2(nums):
    n = len(nums)
    prefix = [1]
    suffix = [1]
    res = [1] * n
    for i in range(n):
        res[i] *= prefix[i]
        prefix.append(prefix[-1] * nums[i])
        res[n-i-1] *= suffix[i]
        suffix.append(suffix[-1] * nums[n-i-1])
    return res

## 0d dp, TC:O(n), SC:O(1)
def productExceptSelf3(nums):
    ans, suf, pre = [1]*len(nums), 1, 1
    for i in range(len(nums)):
        ans[i] *= pre               # prefix product from one end
        pre *= nums[i]
        ans[-1-i] *= suf            # suffix product from other end
        suf *= nums[-1-i]
    return ans