# https://leetcode.com/problems/n-ary-tree-level-order-traversal/


# BFS, TC:O(N), SC:O(N)
def levelOrder(root: 'Node') -> List[List[int]]:
    res = []
    queue = [root]
    while queue and root:
        res.append([])
        leafs = []
        for node in queue:
            res[-1].append(node.val)
            if not node.children: continue
            leafs.extend(node.children)
        queue = leafs
    return res