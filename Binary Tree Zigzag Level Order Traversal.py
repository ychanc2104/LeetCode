# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# first thought, BFS level order traversal, TC:O(N), SC:O(N)
def zigzagLevelOrder(root):

    # BFS
    queue = [root]
    reverse = False
    res = []
    while queue and root:
        if reverse:
            res.append([queue[i].val for i in range(len(queue) - 1, -1, -1)])
        else:
            res.append([node.val for node in queue])
        leafs = []
        for node in queue:
            if node.left:
                leafs.append(node.left)
            if node.right:
                leafs.append(node.right)
        queue = leafs
        reverse = not reverse
    return res


# clean, BFS level order traversal, TC:O(N), SC:O(N)
def zigzagLevelOrder(root):
    # BFS
    queue = [root]
    direction = 1
    res = []
    while queue and root:
        leafs, temp = [], []
        for node in queue:
            temp.append(node.val)
            if node.left:
                leafs.append(node.left)
            if node.right:
                leafs.append(node.right)
        queue = leafs
        res.append(temp[::direction])
        direction *= -1
    return res