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
    # add prev node
    def dfs(node, prev=None):
        if not node: return
        node.prev = prev
        dfs(node.left, node)
        dfs(node.right, node)

    dfs(root)
    # do level-order
    queue = [target]
    visit = set(queue)
    while queue and k:

        leafs = []
        for i in range(len(queue)):
            node = queue[i]
            for n in (node.left, node.right, node.prev):
                if not n or n in visit: continue
                visit.add(n)
                leafs.append(n)
        queue = leafs
        k -= 1
    return [node.val for node in queue]

# dfs + bfs, TC:O(N), SC:O(N)
def distanceK2(root: TreeNode, target: TreeNode, k: int) -> List[int]:
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
    while queue:
        if queue[0][1] == k:
            return [n.val for n, i in queue]
        node, count = queue.popleft()
        for neighbor in (node.parent, node.left, node.right):
            if not neighbor or neighbor in visit:
                continue
            queue.append((neighbor, count + 1))
        visit.add(node)
    return []