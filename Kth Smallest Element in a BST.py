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

# dfs, inorder traversal, TC:O()
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        # inorder: left => root => right
        self.count = 0
        res = []
        def dfs(root):
            if root:
                dfs(root.left)
                self.count += 1
                if self.count==k:
                    res.append(root.val)
                dfs(root.right)
        dfs(root)
        #print(res, self.count)
        return res[0]