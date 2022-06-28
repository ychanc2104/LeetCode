# https://leetcode.com/problems/diameter-of-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# first thought, TC:O(n)
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.res = 0

        def dfs(root, edges):
            if not root:
                return edges + 1

            left = dfs(root.left, edges)
            right = dfs(root.right, edges)
            self.res = max(self.res, left + right)
            return max(left, right) + 1

        dfs(root, -1)
        return self.res


class Solution2:
    def diameterOfBinaryTree(self, root) -> int:
        self.res = 0
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.res = max(self.res, left+right)
            return max(left, right)+1
        dfs(root)
        return self.res