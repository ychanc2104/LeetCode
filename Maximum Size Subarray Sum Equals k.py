# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/


def maxSubArrayLen(nums: List[int], k: int) -> int:
    prefix = {0: -1}
    s = 0
    res = 0
    for i, num in enumerate(nums):
        s += num
        if s - k in prefix:  # pre[x] + k = pre[i], [x,i] is subarray
            # valid subarray
            res = max(res, i - prefix[s - k])
        if s not in prefix: # don't update new value to max subarray length
            prefix[s] = i
    return res