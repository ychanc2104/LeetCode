# https://leetcode.com/problems/house-robber-iii/description/


import functools

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# top-down dp, TC:O(N), SC:O(N)
@functools.lru_cache(None)
def rob(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    res1 = root.val
    if root.left:
        res1 += rob(root.left.left) + rob(root.left.right)
    if root.right:
        res1 += rob(root.right.left) + rob(root.right.right)
    res2 = rob(root.left) + rob(root.right)
    return max(res1, res2)



# TC:O(N), SC:O(N)
def rob2(root: Optional[TreeNode]) -> int:

    def helper(root):
        if not root:
            return (0, 0) # with itself, without itself
        left = helper(root.left)
        right = helper(root.right)
        return (root.val + left[1] + right[1], max(left) + max(right))

    return max(helper(root))