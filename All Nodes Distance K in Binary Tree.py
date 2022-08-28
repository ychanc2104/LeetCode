# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# dfs + bfs, TC:O(N), SC:O(N)
def distanceK(root: TreeNode, target: TreeNode, k: int) -> List[int]:
    # add parent to each node
    def dfs(node, parent=None):
        if not node:
            return
        node.parent = parent
        dfs(node.left, node)
        dfs(node.right, node)
    dfs(root)
    # level-order to bidirectionally expand at target
    if k == 0:
        return [target.val]
    queue = [target]
    res, count, visit = [], 0, set()
    while queue:
        count += 1
        leafs = []
        for node in queue:
            if node.parent and node.parent.val not in visit:
                leafs.append(node.parent)
            if node.left and node.left.val not in visit:
                leafs.append(node.left)
            if node.right and node.right.val not in visit:
                leafs.append(node.right)
            visit.add(node.val)
        if leafs and count == k:
            res.extend([n.val for n in leafs])
            return res
        queue = leafs
    return res

# concise dfs + bfs, TC:O(N), SC:O(N)
def distanceK2(root: TreeNode, target: TreeNode, k: int) -> List[int]:
    # add parent to each node
    def dfs(node, parent=None):
        if not node:
            return
        node.parent = parent
        dfs(node.left, node)
        dfs(node.right, node)
    dfs(root)
    # level-order to bidirectionally expand at target
    if k == 0:
        return [target.val]
    queue = [target]
    count, visit = 0, set()
    while queue:
        count += 1
        leafs = []
        for node in queue:
            for neighbor in (node.parent, node.left, node.right):
                if not neighbor or neighbor in visit:
                    continue
                leafs.append(neighbor)
            visit.add(node)
        if leafs and count == k:
            return [n.val for n in leafs]
        queue = leafs
    return []

# dfs + bfs, TC:O(N), SC:O(N)
def distanceK3(root: TreeNode, target: TreeNode, k: int) -> List[int]:
    # add parent to each node
    def dfs(node, parent=None):
        if not node:
            return
        node.parent = parent
        dfs(node.left, node)
        dfs(node.right, node)

    dfs(root)
    # print(root)
    # level-order to expand at target
    queue = collections.deque([(target, 0)])  # node, count
    visit = set()
    count = 0
    res = []
    while queue:
        if queue[0][1] == k:
            return [n.val for n, i in queue]
        node, count = queue.popleft()
        for neighbor in (node.parent, node.left, node.right):
            if not neighbor or neighbor in visit:
                continue
            queue.append((neighbor, count + 1))
        visit.add(node)
    return res