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

# TC: O(n), SC: O(logn)
def sortedArrayToBST2(nums):
    # -10,-3,0,5,9 => (0,5),2 => l(0,2),1 r(2+1,5),3 => ll(0,1),0 lr(1+1,2),1
    def helper(left, right):
        mid = (left + right) // 2
        if left == right:
            return None
        root = TreeNode(nums[mid])
        # [), left close and right open
        root.left = helper(left, mid)
        root.right = helper(mid + 1, right)
        return root
    return helper(0, len(nums))

# TC: O(n), SC: O(logn), different tree order with sortedArrayToBST2()
def sortedArrayToBST3(nums):
    def helper(left, right):
        mid = (left + right) // 2
        if left > right:
            return None
        root = TreeNode(nums[mid])
        # [], left close and right close
        root.left = helper(left, mid - 1)
        root.right = helper(mid + 1, right)
        return root
    return helper(0, len(nums) - 1)