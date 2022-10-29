#


# first thought, dfs, TC:O(N), SC:O(N)
def goodNodes(root) -> int:
    res = [0]

    def dfs(root, M):
        if not root: return
        M = max(root.val, M)
        if root.val >= M:
            res[0] += 1
        dfs(root.left, M)
        dfs(root.right, M)

    dfs(root, root.val)
    return res[0]