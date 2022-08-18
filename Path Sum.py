# https://leetcode.com/problems/path-sum/
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive dfs, TC:O(N), SC:O(h), h is height of binary tree ~ O(logN)
def hasPathSum(root, targetSum: int) -> bool:
    if not root: return False

    def dfs(root, target):
        if not root:
            return False
        if not root.left and not root.right:
            return target == root.val
        return dfs(root.left, target - root.val) or dfs(root.right, target - root.val)

    return dfs(root, targetSum)