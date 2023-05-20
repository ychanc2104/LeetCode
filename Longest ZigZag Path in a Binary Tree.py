# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/
# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/solutions/531867/java-python-dfs-solution/?orderBy=most_votes

# DFS, TC:O(N), SC:O(logN)
def longestZigZag(root: Optional[TreeNode]) -> int:
    # left=>True, right=>False
    res = 0

    def helper(root, flag, path=1):
        nonlocal res
        if not root:
            return
        res = max(res, path)
        if not flag:  # prev is right
            helper(root.left, True, path + 1)
            helper(root.right, False)
        else:  # prev is left
            helper(root.right, False, path + 1)
            helper(root.left, True)

    helper(root.left, True)
    helper(root.right, False)
    return res