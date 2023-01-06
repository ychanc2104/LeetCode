# https://leetcode.com/problems/binary-tree-vertical-order-traversal/

import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# first thought, dfs, sort by level and index, TC:O(N+NlogN), SC:O(N)
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # +1,-1
        memo = collections.defaultdict(list)
        def dfs(root, level=0, i=0):
            if not root:
                return
            memo[(i, level)].append(root.val)
            dfs(root.left, level+1, i-1)
            dfs(root.right, level+1, i+1)
        dfs(root)
        res = collections.defaultdict(list)
        for idx, l in sorted(memo.keys()): # sort idx(1st) and level(2nd)
            res[idx].extend(memo[(idx, l)])
        return res.values()

# bfs w/o sorting, TC:O(N), SC:O(N)
def verticalOrder2(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    # +1,-1
    memo = collections.defaultdict(list)
    # BFS
    queue = [(root, 0)]
    min_col = float('inf')
    max_col = float('-inf')
    while queue:
        # node, col = queue.popleft()
        leafs = []
        for node, col in queue:
            if not node:
                continue
            memo[col].append(node.val)
            min_col, max_col = min(min_col, col), max(max_col, col)
            leafs.append((node.left, col - 1))
            leafs.append((node.right, col + 1))
        queue = leafs
    return [memo[c] for c in range(min_col, max_col+1)]