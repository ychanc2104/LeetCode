# https://leetcode.com/problems/range-sum-of-bst/description/

# dfs, TC:O(N), SC:O(N)
def rangeSumBST(root: Optional[TreeNode], low: int, high: int) -> int:
    res = [0]

    def dfs(root):
        if not root: return
        if low <= root.val <= high:
            res[0] += root.val
            dfs(root.left)
            dfs(root.right)
        elif root.val < low:
            dfs(root.right)
        elif root.val > high:
            dfs(root.left)

    dfs(root)
    return res[0]