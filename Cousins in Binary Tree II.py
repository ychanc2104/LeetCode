# https://leetcode.com/problems/cousins-in-binary-tree-ii/description/

import collections


# dfs twice, TC:O(N), SC:O(N)
def replaceValueInTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    memo = collections.defaultdict(int)  # depth: sum

    def dfs_sum(root, depth=0):
        if not root:
            return
        memo[depth] += root.val
        dfs_sum(root.left, depth + 1)
        dfs_sum(root.right, depth + 1)

    def helper(root, s=0, depth=0):
        if not root:
            return
        root.val = memo[depth] - s
        s = 0
        if root.left:
            s += root.left.val
        if root.right:
            s += root.right.val
        helper(root.left, s, depth + 1)
        helper(root.right, s, depth + 1)
        return root

    dfs_sum(root)
    return helper(root, root.val)