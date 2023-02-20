# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/

# inorder traversal, dfs, TC:O(N), SC:O(N)
def minDiffInBST(root: Optional[TreeNode]) -> int:
    res = float('inf')
    prev = float('inf')
    # left->root->right => sorted list, so compare every adjacent pair
    def dfs(root):
        nonlocal res, prev
        if not root: return
        dfs(root.left)
        res = min(res, abs(root.val - prev))
        prev = root.val
        dfs(root.right)

    dfs(root)
    return res