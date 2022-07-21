# https://leetcode.com/problems/next-permutation/
# https://leetcode.com/problems/next-permutation/discuss/14054/Python-solution-with-comments.
# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

# def nextPermutation(nums) -> None:
#     """
#     Do not return anything, modify nums in-place instead.
#     """
#     i_nonin = len(nums)
#     for i in range(len(nums)-2, -1, -1):
#         if nums[i] < nums[i+1]:
#             i_nonin = i
#             break
#     if i_nonin==len(nums):
#         nums.reverse()
#         return
#
#     # diff = nums[i_nonin+1] - nums[i_nonin]
#     # i_swap = len(nums)-1
#     j = len(nums) - 1
#     while j >= 0 and nums[i_nonin] > nums[j]:
#         j -= 1
#     i_swap = j
#     # for j in range(i_nonin+1, len(nums)):
#     #     if nums[i_nonin] > nums[j]:
#     #         break
#     # i_swap = j - 1
#     print(i_nonin, i_swap)
#     nums[i_nonin], nums[i_swap] = nums[i_swap], nums[i_nonin]
#     # reverse
#     nums[i_nonin+1:] = nums[i_nonin+1:][::-1]

def nextPermutation2(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = j = len(nums)-1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1
    if i == 0:   # nums are in descending order
        nums.reverse()
        return
    k = i - 1    # find the last "ascending" position
    while nums[j] <= nums[k]:
        j -= 1
    print(k, j)
    nums[k], nums[j] = nums[j], nums[k]
    l, r = k+1, len(nums)-1  # reverse the second part
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l +=1 ; r -= 1

# nums = [0,1,2,5,3,3,0]
# nums = [2,3,1,3,3]
nums = [1,5,1]

nums2 = nums.copy()
nextPermutation(nums)

nextPermutation2(nums2)
