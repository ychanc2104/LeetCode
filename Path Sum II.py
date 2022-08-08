# https://leetcode.com/problems/path-sum-ii/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# first thought, dfs, TC:O(N^2), SC:O(N^2)
def pathSum(root, targetSum: int):
    res = []
    def helper(root, targetSum, path):
        if root:
            # root to a node without children, sum take TC:O(N)
            if not root.left and not root.right and sum(path)==targetSum:
                res.append(path)
                return
            if root.left:
                # creating new list, TC:O(N)
                helper(root.left, targetSum, path + [root.left.val])
            if root.right:
                helper(root.right, targetSum, path + [root.right.val])
    if root:
        helper(root, targetSum, [root.val])
    return res

# recursive dfs + backtracking, faster, TC:O(N^2), SC:O(N^2)
def pathSum2(root, targetSum: int):
    res = []
    def helper(root, targetSum, path):
        if root:
            path.append(root.val)
            # root to a node without children
            if not root.left and not root.right and targetSum - root.val == 0:
                res.append(path[:])
                # backtracking
                path.pop()
                return
            helper(root.left, targetSum - root.val, path)
            helper(root.right, targetSum - root.val, path)
            # backtracking
            path.pop()

    helper(root, targetSum, [])
    return res

# iterative dfs + backtracking, the fastest, TC:O(N^2), SC:O(N^2)
def pathSum3(root, targetSum: int):
    if not root:
        return []
    res = []
    stack = [(root, targetSum - root.val, [root.val])]
    while stack:
        curr, val, ls = stack.pop()
        if not curr.left and not curr.right and val == 0:
            res.append(ls)
        if curr.right:
            stack.append((curr.right, val - curr.right.val, ls + [curr.right.val]))
        if curr.left:
            stack.append((curr.left, val - curr.left.val, ls + [curr.left.val]))
    return res