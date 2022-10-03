# https://leetcode.com/problems/sort-colors/

import collections

# counting sort, TC:O(n), SC:O(1)
def sortColors(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    counter = collections.Counter(nums)
    for i in range(len(nums)):
        if counter[0] > 0:
            nums[i] = 0
            counter[0] -= 1
        elif counter[1] > 0:
            nums[i] = 1
            counter[1] -= 1
        else:
            nums[i] = 2
            counter[2] -= 1

# one-pass, TC:O(n), SC:O(1)
def sortColors2(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    L, R = 0, len(nums) - 1
    i = 0 # checked index
    #
    while i <= R:
        if nums[i] == 2:
            nums[i], nums[R] = nums[R], nums[i]
            R -= 1
        elif nums[i] == 0:
            nums[L], nums[i] = nums[i], nums[L]
            L += 1
            i = L
        elif nums[i] == 1:
            i += 1

# counting sort, TC:O(N), SC:O(3)
def sortColors3(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # 0, 1, 2 only
    counting = [0] * 3
    for num in nums:
        counting[num] += 1
    i = 0
    for v in range(3):
        for _ in range(counting[v]):
            nums[i] = v
            i += 1

