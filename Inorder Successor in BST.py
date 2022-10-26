# https://leetcode.com/problems/inorder-successor-in-bst/
# https://leetcode.com/problems/inorder-successor-in-bst/discuss/72723/Python-Short-Recursive-solution-4-lines
# https://leetcode.com/problems/inorder-successor-in-bst/discuss/72656/JavaPython-solution-O(h)-time-and-O(1)-space-iterative

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive dfs, TC:O(N), SC:O(N) N for recursive call
def inorderSuccessor(root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
    if not root:
        return root
    if root.val <= p.val:
        return inorderSuccessor(root.right, p)
    else:
        temp = inorderSuccessor(root.left, p)
        return temp if temp else root

# iterative dfs, TC:O(N), SC:O(N)
def inorderSuccessor2(root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
    # left=>root=>right
    stack = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if root.val > p.val:
            return root
        root = root.right
    return None

# BST properties, TC:O(N), SC:O(1)
def inorderSuccessor3(root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
    # BST
    res = None
    while root:
        if root.val > p.val:
            # go smaller node
            res = root
            root = root.left
        else:
            # go larger node
            root = root.right
    return res