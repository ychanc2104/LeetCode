# https://leetcode.com/problems/number-of-zero-filled-subarrays/description/



# first thought, sliding window, TC:O(N), SC:O(1)
def zeroFilledSubarray(nums: List[int]) -> int:
    # maintain a sliding window
    n = len(nums)
    L = 0
    res = 0
    while L < n:

        if nums[L] != 0:
            L += 1
            continue
        R = L
        while R < n and nums[R] == 0:
            res += R - L + 1
            R += 1
        L = R + 1
    return res

# two pointers, TC:O(N), SC:O(1)
def zeroFilledSubarray2(nums: List[int]) -> int:
    n = len(nums)
    res = 0
    L = 0
    for R in range(n):
        if nums[R]: # not 0
            L = R + 1
        res += R - L + 1
    return res

# TC:O(N), SC:O(1)
def zeroFilledSubarray3(nums: List[int]) -> int:
    res = 0
    zero_array_len = 0
    for num in nums:
        if num == 0:
            zero_array_len += 1
        else:
            zero_array_len = 0
        res += zero_array_len
    return res
