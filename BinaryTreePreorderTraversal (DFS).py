# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## order: node => left => right
# time: O(n), Space: worst, O(n), average, O(logn) (height of binary tree or in balanced tree)

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
    def preorderTraversal2(self, root):
        ## dfs
        ans = []
        if root:
            ans.append(root.val)
            ans.extend(self.preorderTraversal(root.left))
            ans.extend(self.preorderTraversal(root.right))
        return ans

    ## recursive
    def preorderTraversal3(self, root):
        # root => left => right
        res = []
        def dfs(root):
            if root:
                res.append(root.val)
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return res