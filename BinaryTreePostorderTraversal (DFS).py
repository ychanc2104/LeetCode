# https://leetcode.com/problems/binary-tree-postorder-traversal/
# https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45785/Share-my-two-Python-iterative-solutions-post-order-and-modified-preorder-then-reverse
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## order: left => right => node

# time: O(n), Space: worst, O(n), average, O(logn) (height of binary tree or in balanced tree)

class Solution:
    ## iterative method
    def postorderTraversal(self, root):
        stack = [root]
        ans = []
        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return ans[::-1]
    ## iterative method
    def postorderTraversal2(self, root):
        stack = [(root, False)]
        ans = []
        while stack:
            node, status = stack.pop()
            if node:
                if status:
                    ans.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return ans

    ## recursive method
    def postorderTraversal3(self, root):
        ans = []
        if root:
            ans.extend(self.postorderTraversal(root.left))
            ans.extend(self.postorderTraversal(root.right))
            ans.append(root.val)
        return ans

    ## iteratvie method
    def postorderTraversal4(self, root):
        # left => right => root
        res = []
        stack = [(root, False)]
        while stack:
            root, visited = stack.pop()
            if root:
                # print(root.val)
                if visited:
                    res.append(root.val)
                else:
                    # first in last out
                    stack.append((root, True))
                    stack.append((root.right, False))
                    # left, last in first out
                    stack.append((root.left, False))
        return res