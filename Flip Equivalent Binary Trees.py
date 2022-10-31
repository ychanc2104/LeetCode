# https://leetcode.com/problems/flip-equivalent-binary-trees/description/

import itertools

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# first thought, TC:O(min(N,M)), SC:O(min(N,M))
def flipEquiv(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    if not root1 and not root2: return True
    if not root1 or not root2: return False
    if root1.val == root2.val:
        # test left and rigth
        Lflip = flipEquiv(root1.left, root2.right)
        Rflip = flipEquiv(root1.right, root2.left)
        Lnoflip = flipEquiv(root1.left, root2.left)
        Rnoflip = flipEquiv(root1.right, root2.right)
        return (Lflip and Rflip) or (Lnoflip and Rnoflip)
    return False


# refine, TC:O(min(N,M)), SC:O(min(N,M))
def flipEquiv2(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    if not root1 and not root2: return True
    if not root1 or not root2: return False
    # test left and rigth
    return (root1.val == root2.val) and (flipEquiv2(root1.left, root2.right) and flipEquiv2(root1.right, root2.left)) \
    or (flipEquiv2(root1.left, root2.left) and flipEquiv2(root1.right, root2.right))


