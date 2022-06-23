# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/discuss/64963/3-lines-with-O(1)-space-1-Liners-Alternatives


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# iterative
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

# iterative
def lowestCommonAncestor2(root, p, q):
    m = min(p.val, q.val)
    M = max(p.val, q.val)
    while root:
        if root.val < m:
            # go right
            root = root.right
        elif root.val > M:
            # go left
            root = root.left
        else:
            return root
# recursive
def lowestCommonAncestor3(root, p, q):
    if p.val < root.val > q.val:
        # go left
        return lowestCommonAncestor3(root.left, p, q)
    elif p.val > root.val < q.val:
        # go right
        return lowestCommonAncestor3(root.right, p, q)
    else:
        return root