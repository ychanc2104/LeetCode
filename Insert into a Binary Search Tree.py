# https://leetcode.com/problems/insert-into-a-binary-search-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TC:O(H), SC:O(1)
def insertIntoBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    node = TreeNode(val)
    if not root:
        return node
    dummy = root
    prev = None
    while root:
        prev = root
        if root.val > val:
            root = root.left
        else:
            root = root.right

    if prev.val > val:
        prev.left = node
    else:
        prev.right = node
    return dummy