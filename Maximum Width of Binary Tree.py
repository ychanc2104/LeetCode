# https://leetcode.com/problems/maximum-width-of-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# level-order BFS, TC:O(N), SC:O(N)
def widthOfBinaryTree(root) -> int:
    count = 1
    queue = [(root, 1)]
    while queue:
        leafs = []
        for node, level in queue:
            if node.left:
                leafs.append((node.left, 2 * level))
            if node.right:
                leafs.append((node.right, 2 * level + 1))
        if leafs:
            count = max(count, leafs[-1][1] - leafs[0][1] + 1)
        queue = leafs
    return count