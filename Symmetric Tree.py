# https://leetcode.com/problems/symmetric-tree/

import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# first thought, use isSameTree, TC:O(n), SC:O(logn) or O(n) (linear tree)
def isSymmetric(root) -> bool:
    # check root.left and root.right is same tree?
    # symmetric version
    def sameTree(p, q):
        if p and q and p.val == q.val:
            # compare left and right
            return sameTree(p.left, q.right) and sameTree(p.right, q.left)
        elif not p and not q:
            return True
        else:
            return False
    return sameTree(root.left, root.right)

# iterative dfs, TC:O(n), SC:O(logn) or O(n) (linear tree)
def isSymmetric2(root) -> bool:
    p, q = root.left, root.right
    stack1 = []
    stack2 = []
    while p or q or stack1 or stack2:
        while p or q:
            if (not p and q) or (p and not q) or (p.val != q.val):
                return False
            stack1.append(p)
            p = p.left
            stack2.append(q)
            q = q.right

        p = stack1.pop()
        q = stack2.pop()
        p = p.right
        q = q.left
    return True



# iterative bfs, level-order traversal, TC:O(n), SC:O(logn) or O(n) (linear tree)
def isSymmetric3(root) -> bool:
    queue = collections.deque([root.left, root.right])
    while queue:
        p = queue.popleft()
        q = queue.popleft()
        if not p and not q:
            continue
        if (not p and q) or (p and not q) or (p.val != q.val):
            return False
        queue.append(p.left)
        queue.append(q.right)
        queue.append(p.right)
        queue.append(q.left)

    return True