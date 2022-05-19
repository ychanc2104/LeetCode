# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## order: left => node => right
class Solution:
    ## recursive
    def inorderTraversal(self, root):
        if not root:
            return []
        results = []
        if root.left:
            results.extend(self.inorderTraversal(root.left))
        if root:
            results.extend([root.val])
        if root.right:
            results.extend(self.inorderTraversal(root.right))
        return results

    ## recursive-2
    def inorderTraversal2(self, root):
        res = []
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)

    ## recursive-3
    def inorderTraversal3(self, root):
        results = []
        if root:
            results.extend(self.inorderTraversal(root.left))
            results.extend([root.val])
            results.extend(self.inorderTraversal(root.right))
        return results

    ## iterative method
    def inorderTraversal4(self, root):
        stack = []
        node = root
        ans = []
        while stack or node:
            ## appending loop
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            ans.append(node.val)
            node = node.right
        return ans
