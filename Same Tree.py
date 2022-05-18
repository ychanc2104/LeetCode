# https://leetcode.com/problems/same-tree/
# https://leetcode.com/problems/same-tree/discuss/32729/Shortest%2Bsimplest-Python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSameTree(p, q) -> bool:
    queue = [[p ,q]]
    while queue:
        p, q = queue.pop(0)

        if p and q:
            if p.val!=q.val:
                return False
            queue.append([p.left, q.left])
            queue.append([p.right, q.right])
        elif (p and not q) or (q and not p) :
            return False
    return True

# recursive
def isSameTree2(p, q) -> bool:
    if p and q:
        return p.val==q.val and isSameTree2(p.left,q.left) and isSameTree2(p.right,q.right)
    elif p or q:
        return False
    else:
        return True