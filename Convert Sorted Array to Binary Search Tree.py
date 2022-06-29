# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# first thought, TC: O(nlogn), SC: O(n)
def sortedArrayToBST(nums):
    if not nums:
        return None
    mid = len(nums)//2
    root = TreeNode(nums[mid])
    # O(logn) for slicing
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    return root