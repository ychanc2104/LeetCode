# https://leetcode.com/problems/delete-nodes-and-return-forest/description/


# dfs to return True/False or Node/None, TC:O(N), SC:O(N)
def delNodes(root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
    res = []
    to_delete_set = set(to_delete)

    def dfs(root):
        if not root:
            return None
        root.left = dfs(root.left)
        root.right = dfs(root.right)
        if root.val in to_delete_set:
            if root.left:
                res.append(root.left)
            if root.right:
                res.append(root.right)
            return None
        return root

    if dfs(root):
        res.append(root)
    return res