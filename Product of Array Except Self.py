# https://leetcode.com/problems/product-of-array-except-self/
# https://leetcode.com/problems/product-of-array-except-self/discuss/1342916/3-Minute-Read-Mimicking-an-Interview
# https://leetcode.com/problems/product-of-array-except-self/discuss/1597994/C%2B%2BPython-4-Simple-Solutions-w-Explanation-or-Prefix-and-Suffix-product-O(1)-space-approach


# TC:O(n), SC:O(n)
def productExceptSelf(nums):
    n = len(nums)
    res = []
    left = [1] * n
    right = [1] * n
    for i in range(n):
        # left[i] = a0*a1*...*a(i-1)
        if i == 0:
            left[i] = 1
        else:
            left[i] = left[i - 1] * nums[i - 1]
        if n - 1 - i == n - 1:
            right[n - 1 - i] = 1
        else:
            right[n - 1 - i] = right[n - 1 - i + 1] * nums[n - 1 - i + 1]
    for l, r in zip(left, right):
        res.append(l * r)
    return res

# TC:O(n), SC:O(n),
def productExceptSelf2(nums):
    n = len(nums)
    res = []
    left, right = [0] * n, [0] * n
    left[0], right[-1] = 1, 1
    for i in range(1, n):
        # left[i] = a0*a1*...*a(i-1)
        # right[i] = a(i+1)*...*a(n-1)
        left[i] = left[i - 1] * nums[i - 1]
        right[-1 - i] = right[-1 - i + 1] * nums[-1 - i + 1]
    for l, r in zip(left, right):
        res.append(l * r)
    return res

## use prefix and suffix, TC:O(n), SC:O(1)
def productExceptSelf3(nums):
    ans, suf, pre = [1]*len(nums), 1, 1
    for i in range(len(nums)):
        ans[i] *= pre               # prefix product from one end
        pre *= nums[i]
        ans[-1-i] *= suf            # suffix product from other end
        suf *= nums[-1-i]
    return ans