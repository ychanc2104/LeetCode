# https://leetcode.com/problems/validate-binary-search-tree/
# https://leetcode.com/problems/validate-binary-search-tree/discuss/146601/Python3-100-using-easy-recursion


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## left => node => right
class Solution:
    ## recursive
    def isValidBST(self, root) -> bool:
        # res = []
        self.last = float("-inf")
        self.valid = True

        def dfs(root):

            if root:
                # print(root.val)
                dfs(root.left)
                if root.val <= self.last:
                    self.valid = False
                    return
                self.last = root.val
                dfs(root.right)

        dfs(root)
        # print(res)
        return self.valid

    ## iterrative
    def isValidBST2(self, root) -> bool:

        stack = []
        node = root
        last = float('-inf')
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            # print(node.val, last)
            if node.val <= last:
                return False
            last = node.val
            node = node.right
        return True
    def isValidBST3(self, root) -> bool:

        def check_bst(node, left, right):

            if not node:
                return True
            # print(node.val)
            if not left < node.val < right:
                print(left, node.val, right)
                return False
            # update right bound for left node checking, update left bound for right node checking
            return (check_bst(node.left, left, node.val)
                    and check_bst(node.right, node.val, right))

        return check_bst(root, float("-inf"), float("inf"))

    def isValidBST4(self, root) -> bool:
        def dfs(root, left, right):
            if not root:
                return True

            if not (left < root.val < right):
                return False

            return dfs(root.left, left, root.val) and dfs(root.right, root.val, right)

        return dfs(root, float("-inf"), float("inf"))
