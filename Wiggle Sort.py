# https://leetcode.com/problems/wiggle-sort/


# first thought, sorting, TC:O(NlogN), SC:O(N) for sorting
def wiggleSort(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    nums.sort()
    for i in range(n - 1):
        if i % 2 == 1:
            # swap
            nums[i], nums[i + 1] = nums[i + 1], nums[i]



# greedy, TC:O(N), SC:O(1)
def wiggleSort2(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    for i in range(n-1):
        if i % 2 == 0 and nums[i] > nums[i+1]:
            # swap
            nums[i], nums[i+1] = nums[i+1], nums[i]
        elif i % 2 == 1 and nums[i] < nums[i+1]:
            # swap
            nums[i], nums[i+1] = nums[i+1], nums[i]