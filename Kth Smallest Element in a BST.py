# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## first thought
def kthSmallest(root, k: int) -> int:

    # left => root => right
    stack = [] ## or deque([]) will be faster
    res = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.append(root.val)
        root = root.right
    return res[k - 1]

def kthSmallest2(root, k: int) -> int:
    # left => root => right (inorder)
    stack = deque([])
    i = 0
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if i + 1 == k:
            return root.val
        i += 1
        root = root.right