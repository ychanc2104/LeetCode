# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def lowestCommonAncestor(root, p, q):
    m = min(p.val, q.val)
    M = max(p.val, q.val)
    while root:
        if m <= root.val <= M:
            return root
        elif root.val < m:
            # go right
            root = root.right
        elif root.val > M:
            # go left
            root = root.left


