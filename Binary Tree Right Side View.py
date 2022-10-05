# https://leetcode.com/problems/binary-tree-right-side-view/


# first thought, level order traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# level order traversal, TC:O(N), SC:O(D) D is diameter of tree
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


# dfs, TC:O(N), SC:O(H) H is height of tree
def rightSideView2(root):
    if not root:
        return []
    res = []
    def helper(root, level=0):

        if len(res) <= level:
            res.append(root.val)
        if root and root.right:
            helper(root.right, level+1)
        if root and root.left:
            helper(root.left, level+1)

    helper(root, 0)
    return res