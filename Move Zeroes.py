# https://leetcode.com/problems/move-zeroes/
# https://leetcode.com/problems/move-zeroes/discuss/72012/Python-short-in-place-solution-with-comments.

# first thought
def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for num in nums:
        if num == 0:
            nums.remove(0)
            nums.append(0)


# reduce useless operation
def moveZeroes2(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    i = 0
    for _ in range(n):
        if nums[i] == 0:
            nums.remove(0)
            nums.append(0)
        else:
            i += 1

# TC: O(n), SC:O(1)
def moveZeroes3(nums) -> None:
    # position of zero
    i_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[i_zero] = nums[i_zero], nums[i]
            i_zero += 1