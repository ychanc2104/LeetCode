# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# first thought, TC:O(N^2), SC:O(logN)
def buildTree(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    # left=>root=>right
    # left=>right=>root

    def helper(L, R):
        if L > R:
            return None

        root = TreeNode(postorder.pop())
        idx = inorder.index(root.val)
        root.right = helper(idx + 1, R)
        root.left = helper(L, idx - 1)
        return root

    return helper(0, len(inorder) - 1)

# build lookup table, TC:O(N), SC:O(logN)
def buildTree2(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    # left=>root=>right
    # left=>right=>root
    memo = {v: i for i, v in enumerate(inorder)}

    def helper(L, R):
        if L > R:
            return None

        root = TreeNode(postorder.pop())
        idx = memo[root.val]
        root.right = helper(idx + 1, R)
        root.left = helper(L, idx - 1)
        return root

    return helper(0, len(inorder) - 1)