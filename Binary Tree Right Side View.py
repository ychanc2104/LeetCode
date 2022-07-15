# https://leetcode.com/problems/binary-tree-right-side-view/


# first thought, level order traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# level order traversal, TC:O(N), SC:O(2^h)
def rightSideView(root):
    # rightmost node, level order and pick rightmost
    res = []
    levels = [root]
    while levels and root:
        res.append(levels[-1].val)
        leafs = []
        for l in levels:
            if l.left:
                leafs.append(l.left)
            if l.right:
                leafs.append(l.right)
        levels = leafs
    return res