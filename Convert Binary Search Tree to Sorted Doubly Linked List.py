# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# first thought, dfs,
def treeToDoublyList(root: 'Optional[Node]') -> 'Optional[Node]':
    if not root: return None
    head = dummy = Node(0)
    def dfs(root):
        nonlocal head
        # inorder
        if not root: return
        dfs(root.left)
        head.right = Node(root.val, left=head)
        head = head.right
        dfs(root.right)
    dfs(root)
    dummy = dummy.right
    dummy.left = head
    head.right = dummy
    return dummy