# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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



