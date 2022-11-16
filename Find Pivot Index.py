# https://leetcode.com/problems/find-pivot-index/description/

# prefix sum, TC:O(N), SC:O(1)
def pivotIndex(nums: List[int]) -> int:
    S = sum(nums)
    prefix_sum = 0
    for i, num in enumerate(nums):
        if S - prefix_sum - num == prefix_sum:  # right == left
            return i
        prefix_sum += num
    return -1