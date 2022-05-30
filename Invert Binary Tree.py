# https://leetcode.com/problems/invert-binary-tree/
# https://leetcode.com/problems/invert-binary-tree/discuss/62714/3-4-lines-Python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# first thought, bfs
def invertTree(root):
    queue = [root]
    while queue:

        node = queue.pop(0)
        if node:
            queue.append(node.left)
            queue.append(node.right)
            node.left, node.right = node.right, node.left
    return root

# recursive dfs
def invertTree2(root):
    if root:
        root.left, root.right = root.right, root.left
        invertTree2(root.left)
        invertTree2(root.right)
    return root

def invertTree3(root):
    if root:
        root.left, root.right = invertTree3(root.right), invertTree3(root.left)
    return root