# https://leetcode.com/problems/convert-bst-to-greater-tree/description/

# dfs, TC:O(N), SC:O(N)
def convertBST(root: Optional[TreeNode]) -> Optional[TreeNode]:
    s = 0

    def dfs(root):
        nonlocal s
        if not root: return
        dfs(root.right)
        root.val += s
        s = root.val
        dfs(root.left)

    dfs(root)
    return root