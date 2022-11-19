# https://leetcode.com/problems/two-sum-less-than-k/

import bisect

# first thought, TC:O(N^2), SC:O(1)
def twoSumLessThanK(nums: list[int], k: int) -> int:
    res = -1
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] >= k:
                continue
            res = max(res, nums[i] + nums[j])
    return res

# sorting + two pointers, TC:O(NlogN), SC:O(N) for sorting
def twoSumLessThanK2(nums: list[int], k: int) -> int:
    nums.sort()
    L, R = 0, len(nums)-1
    res = -1
    while L < R:
        target = nums[L] + nums[R]
        if target >= k:
            R -= 1
        else:
            L += 1
            res = max(res, target)
    return res

# sorting + binary search, TC:O(NlogN), SC:O(N) for sorting
def twoSumLessThanK3(nums: list[int], k: int) -> int:
    def bsearch(nums, target, L_initial=0): # leftmost, equivalent to bisect.bisec
        # 1,3,5,7,9 find 4
        L, R = L_initial, len(nums) - 1
        while L <= R:
            mid = (L + R)//2
            if nums[mid] >= target:
                R = mid - 1
            else:
                L = mid + 1
        return L - 1

    nums.sort()
    res = -1
    for i in range(len(nums)):
        idx = bsearch(nums, k-nums[i], i)
        if idx > i:
            res = max(res, nums[i] + nums[idx])
    return res

def bsearch(nums, target, L_initial=0): # leftmost, equivalent to bisect.bisect_left() - 1
    # 1,3,5,7,9 find 4
    L, R = L_initial, len(nums) - 1
    while L <= R:
        mid = (L + R)//2
        if nums[mid] >= target:
            R = mid - 1
        else:
            L = mid + 1
    return L - 1

nums = [1,3,5,7,9]
target = 4
i1 = bsearch(nums, target)
i2 = bisect.bisect_left(nums, target)