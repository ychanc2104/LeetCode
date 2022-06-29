# https://leetcode.com/problems/symmetric-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# first thought, use isSameTree, TC:O(n), SC:O(logn) or O(n) (linear tree)
def isSymmetric(root) -> bool:
    # check root.left and root.right is same tree?
    # symmetric version
    def sameTree(p, q):
        if p and q and p.val == q.val:
            # compare left and right
            return sameTree(p.left, q.right) and sameTree(p.right, q.left)
        elif not p and not q:
            return True
        else:
            return False
    return sameTree(root.left, root.right)
