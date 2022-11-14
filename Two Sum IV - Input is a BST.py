# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/

# hash, TC:O(N), SC:O(N)
def findTarget(root: Optional[TreeNode], k: int) -> bool:
    hash_set = set()

    def dfs(root):
        if not root: return False
        if root.val in hash_set:
            return True
        hash_set.add(k - root.val)
        return dfs(root.left) or dfs(root.right)

    return dfs(root)