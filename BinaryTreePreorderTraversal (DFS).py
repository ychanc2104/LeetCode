# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ## iterative
    def preorderTraversal(self, root):
        ## dfs
        stack = []
        ans = []
        node = root
        while stack or node:
            while node:
                ans.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return ans

    ## recursive
    def preorderTraversal(self, root):
        ## dfs
        ans = []
        if root:
            ans.append(root.val)
            ans.extend(self.preorderTraversal(root.left))
            ans.extend(self.preorderTraversal(root.right))
        return ans
