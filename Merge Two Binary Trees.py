# https://leetcode.com/problems/merge-two-binary-trees/description/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# first thought, create another tree, O(max(N,M)), SC:O(max(N,M))
def mergeTrees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root1 and not root2: return None
    root = TreeNode((root1.val if root1 else 0) + (root2.val if root2 else 0))
    root.left = mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
    root.right = mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
    return root


# use existing tree, O(max(N,M)), SC:O(max(N,M))
def mergeTrees2(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root1 or not root2: return root1 or root2
    root1.val += (root2.val if root2 else 0)
    root1.left = mergeTrees2(root1.left if root1 else None, root2.left if root2 else None)
    root1.right = mergeTrees2(root1.right if root1 else None, root2.right if root2 else None)
    return root1