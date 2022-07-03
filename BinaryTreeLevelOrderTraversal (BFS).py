# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        roots = [root]
        leafs, results = [], []
        while roots or leafs:
            nodes = []
            ## collecting leafs at the same level
            for r in roots:
                if r.left:
                    leafs.append(r.left)
                if r.right:
                    leafs.append(r.right)
                if r:
                    nodes.append(r.val)
            results.append(nodes)
            ## use leafs as levels in the next round
            roots, leafs = leafs, []
        return results

    def levelOrder2(self, root):
        level, results = [root], []
        while root and level:
            results.append([l.val for l in level])
            ## get leafs in the same level
            leafs = [[l.left, l.right] for l in level]
            ## get level of each leafs
            level = [l for LR in leafs for l in LR if l]
        return results

    def levelOrder3(self, root):
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

    def levelOrder3(self, root):
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

    def levelOrder4(self, root):
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