# https://leetcode.com/problems/balanced-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# first thought, dfs, slow
class Solution:
    def isBalanced(self, root) -> bool:
        self.res = True
        if not root:
            return True
        def dfs(root, count):
            if root:
                left = dfs(root.left, count+1)
                right = dfs(root.right, count+1)
                self.res = self.res and -1<=left-right<=1
                if self.res:
                    return max(dfs(root.left, count+1), dfs(root.right, count+1))
                else:
                    return count+1
            else:
                return count
        dfs(root, 0)
        return self.res
