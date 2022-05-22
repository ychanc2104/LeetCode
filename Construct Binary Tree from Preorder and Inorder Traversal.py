# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34613/A-Python-recursive-solution


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# time: O(n^2)
def buildTree(preorder, inorder):
    # pre: root=>left=>right
    # in : left=>root=>right
    if not (preorder and inorder):
        return None

    root = TreeNode(preorder[0])
    # time: O(n)
    i = inorder.index(preorder[0])  # length of left
    # time : O(n)
    root.left = buildTree(preorder[1:i + 1], inorder[:i])
    root.right = buildTree(preorder[i + 1:], inorder[i + 1:])

    return root

def buildTree2(preorder, inorder):
    # pre: root=>left=>right
    # in : left=>root=>right
    # TC: O(n) on avg
    inorder_idx = {val: idx for idx, val in enumerate(inorder)}
    def helper(left, right):
        # no node case
        if left > right:
            return None
        # print(left,right)
        root = TreeNode(preorder.pop(0))
        # O(1) avg
        idx = inorder_idx[root.val]
        # left node is index between 0 and idx-1
        root.left = helper(left, idx - 1)
        # right node is index between idx+1 and n-1
        root.right = helper(idx + 1, right)
        return root
    return helper(0, len(inorder) - 1)


def buildTree3(preorder, inorder):

    def build(stop):
        if inorder and inorder[-1] != stop:
            root = TreeNode(preorder.pop())
            # print(root.val)
            root.left = build(root.val)
            inorder.pop()
            root.right = build(stop)
            return root
    preorder.reverse()
    inorder.reverse()
    return build(None)

