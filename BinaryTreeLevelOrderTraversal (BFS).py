# https://leetcode.com/problems/binary-tree-level-order-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

# bfs, TC:O(n), SC:O(n)
def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
        return []
    queue = [root]
    res = []
    while queue:
        res.append([node.val for node in queue])
        leafs = []
        for node in queue:
            if node.left:
                leafs.append(node.left)
            if node.right:
                leafs.append(node.right)
        queue = leafs
    return res


# dfs, TC:O(n), SC:O(n)
def levelOrder2(root):
    res = []
    def dfs(root, level):
        if not root: return
        if len(res) <= level:
            res.append([])
        res[level].append(root.val)
        dfs(root.left, level + 1)
        dfs(root.right, level + 1)
    dfs(root, 0)
    return res



def levelOrder3(root):
    ans = []
    levels = [root]
    while levels and root:
        ## append ans
        ans.append([node.val for node in levels if node])
        ## collecting leafs
        leafs = [[node.left, node.right] for node in levels if node]
        ## deconstruct leafs as levels next round
        levels = [node for LR in leafs for node in LR if node]
    return ans

def levelOrder4(root):
    level = 0
    prelevel = -1
    res = []
    ans = []
    node = root
    queue = collections.deque([[node, level]])
    while queue and node:
        node, level = queue.popleft()
        if ans and prelevel != level:
            res.append(ans)
            ans = []
        if node:
            ans.append(node.val)
        if node.left:
            queue.append([node.left, level+1])
        if node.right:
            queue.append([node.right, level+1])
        prelevel = level
    if ans:
        res.append(ans)
    return res

def levelOrder5(root):
    level, prelevel = 0, -1
    res, ans = [], []
    queue = collections.deque([[root, level]])
    while queue:
        node, level = queue.popleft()
        if ans and prelevel != level:
            res.append(ans)
            ans = []
        if node:
            ans.append(node.val)
            queue.append([node.left, level+1])
            queue.append([node.right, level+1])
        prelevel = level

    return res

def levelOrder6(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    levels = []
    if not root:
        return levels

    level = 0
    queue = collections.deque([root])
    while queue:
        # start the current level
        levels.append([])
        # number of elements in the current level
        level_length = len(queue)

        for i in range(level_length):
            node = queue.popleft()
            # fulfill the current level
            levels[level].append(node.val)

            # add child nodes of the current level
            # in the queue for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # go to next level
        level += 1
    return levels