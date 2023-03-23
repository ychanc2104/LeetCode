# https://leetcode.com/problems/clone-binary-tree-with-random-pointer/description/

# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

# TC:O(N), SC:O(N)
def copyRandomBinaryTree(root: 'Optional[Node]') -> 'Optional[NodeCopy]':
    memo = {}

    def helper(root):
        if not root:
            return None
        if root in memo:
            return memo[root]
        node = NodeCopy(root.val)
        memo[root] = node
        node.random = helper(root.random)
        node.left = helper(root.left)
        node.right = helper(root.right)

        return node

    return helper(root)