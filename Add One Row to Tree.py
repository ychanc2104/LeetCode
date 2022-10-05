# https://leetcode.com/problems/add-one-row-to-tree/description/


# first thought dfs

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# dfs, TC:O(D), SC:O(D)
def addOneRow(root, val: int, depth: int):
    if depth == 1:
        return TreeNode(val, left=root)

    def helper(root, level=1):
        if not root or level >= depth:
            return root
        if level == depth-1:
            root.left = TreeNode(val, left=root.left)
            root.right = TreeNode(val, right=root.right)
            return root
        root.left = helper(root.left, level+1)
        root.right = helper(root.right, level+1)
        return root
    return helper(root)

# bfs, TC:O(D), SC:O(D)
def addOneRow2(root, val: int, depth: int):
    if depth == 1:
        return TreeNode(val, left=root)

    queue = [root]
    level = 2
    while queue:
        if level == depth:
            for node in queue:
                # level order
                node.left = TreeNode(val, left=node.left)
                node.right = TreeNode(val, right=node.right)
            return root
        leafs = []
        for node in queue:
            if node.left:
                leafs.append(node.left)
            if node.right:
                leafs.append(node.right)
        queue = leafs
        level += 1
    return root