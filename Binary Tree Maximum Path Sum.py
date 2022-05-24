# https://leetcode.com/problems/binary-tree-maximum-path-sum/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def maxPathSum(root) -> int:
    res = root.val

    def dfs(root):
        # use res in maxPathSun
        nonlocal res
        if not root:
            return 0
        maxLeft = max(dfs(root.left), 0)
        maxRight = max(dfs(root.right), 0)
        # update res if greater than res
        res = max(res, root.val + maxLeft + maxRight)
        # choose max path to return
        return root.val + max(maxLeft, maxRight)

    dfs(root)
    return res