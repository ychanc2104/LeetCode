# https://leetcode.com/problems/find-leaves-of-binary-tree/description/


# dfs, TC:O(N), SC:O(N)
def findLeaves(root: Optional[TreeNode]) -> List[List[int]]:
    res = []

    def dfs(root):
        if not root: return -1
        L = dfs(root.left)
        R = dfs(root.right)
        height = max(L, R) + 1
        if height >= len(res):
            res.append([root.val])
        else:
            res[height].append(root.val)
        return height

    dfs(root)
    return res