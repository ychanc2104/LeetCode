# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/
# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/solutions/2708099/java-c-python-sliding-window-with-explanation/



# sliding window, three pointers, TC:O(N), SC:O(1)
def countSubarrays(nums: List[int], minK: int, maxK: int) -> int:
    imin, imax = -1, -1
    iout = -1
    n = len(nums)
    res = 0
    for i in range(n):
        if nums[i] < minK or nums[i] > maxK:
            iout = i
        if nums[i] == minK:
            imin = i
        if nums[i] == maxK:
            imax = i
        res += max(0, min(imin, imax) - iout)
    return res