# https://leetcode.com/problems/subarray-product-less-than-k/

import math

# brute force, TC:O(N^2), SC:O(1)
def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    # 1+2+2+3
    n = len(nums)
    res = 0
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= nums[j]
            if product < k:
                res += 1
    return res

# sliding window, only valid for all numbers > 0, TC:O(N), SC:O(1)
def numSubarrayProductLessThanK2(nums: List[int], k: int) -> int:
    # 1+2+2+3
    if k <= 1: return 0  # nums[i] >= 1
    L = 0
    n = len(nums)
    product = 1
    res = 0
    for R in range(n):  # end with R
        product *= nums[R]
        while product >= k:  # find L
            product //= nums[L]
            L += 1
        res += R - L + 1  # window size
    return res

# prefix product + binary search (TLE), TC:O(nlogn), SC:O(n)
def numSubarrayProductLessThanK3(nums: List[int], k: int) -> int:
    # 1+2+2+3
    if k <= 1: return 0 # nums[i] >= 1
    prefix = []
    p = 1
    for num in nums:
        p *= num
        prefix.append(p)
    def bsearch(target, R):
        L = 0
        while L <= R:
            mid = (L + R)//2
            if prefix[mid] >= target:
                R = mid - 1
            else:
                L = mid + 1
        return L # [0,len(prefix)]
    res = 0
    for i,pre in enumerate(prefix):
        target = pre//k+1
        idx = bsearch(target, i) # left bound
        res += i-idx+1 if target == 1 else i-idx
    return res

# prefix sum + binary search(accepted), TC:O(nlogn), SC:O(n)
def numSubarrayProductLessThanK4(nums: List[int], k: int) -> int:
    # 1+2+2+3
    if k <= 1: return 0 # nums[i] >= 1
    prefix = []
    s = 0
    for num in nums:
        s += math.log(num)
        prefix.append(s)
    def bsearch(target, R):
        L = 0
        while L <= R:
            mid = (L + R)//2
            if prefix[mid] >= target:
                R = mid - 1
            else:
                L = mid + 1
        return L # [0,len(prefix)]
    res = 0
    logk = math.log(k)
    for i,pre in enumerate(prefix):
        target = pre - logk + 10**(-6) # let target become slightly bigger
        idx = bsearch(target, i) # left bound, find first element > target
        res += i-idx+1 if target < 0 else i-idx
    return res