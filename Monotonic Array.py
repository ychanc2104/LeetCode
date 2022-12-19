# https://leetcode.com/problems/monotonic-array/description/

# two pass, TC:O(N), SC:O(1)
def isMonotonic(nums: List[int]) -> bool:
    n = len(nums)
    if n == 1: return True
    return all(nums[i + 1] >= nums[i] for i in range(n - 1)) or all(nums[i + 1] <= nums[i] for i in range(n - 1))

# one pass, TC:O(N), SC:O(1)
def isMonotonic(nums: List[int]) -> bool:
    n = len(nums)
    increase = True
    decrease = True
    for i in range(n-1):
        diff = nums[i+1] - nums[i]
        if diff > 0:
            decrease = False
        elif diff < 0:
            increase = False
    return increase or decrease