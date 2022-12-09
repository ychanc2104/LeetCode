# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# first thought, TC:O(N), SC:O(logN)
def maxAncestorDiff(root: Optional[TreeNode]) -> int:
    res = [0]

    def dfs(root):
        # return min and max
        if not root: return float("inf"), float("-inf")
        ml, Ml = dfs(root.left)
        mr, Mr = dfs(root.right)
        res[0] = max(res[0], abs(root.val - min(ml, root.val)), abs(root.val - max(Ml, root.val)),
                     abs(root.val - min(mr, root.val)), abs(root.val - max(Mr, root.val)))
        return min(ml, mr, root.val), max(Ml, Mr, root.val)

    dfs(root)
    return res[0]

# update min and max along path, TC:O(N), SC:O(logN)
def maxAncestorDiff2(root: Optional[TreeNode]) -> int:
    def helper(root, low, high):
        # return diff of this path
        if not root: return high - low
        # update low and high along path
        low = min(root.val, low)
        high = max(root.val, high)
        left = helper(root.left, low, high)
        right = helper(root.right, low, high)
        return max(left, right)

    return helper(root, root.val, root.val)