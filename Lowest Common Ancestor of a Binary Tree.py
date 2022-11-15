# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# https://www.youtube.com/watch?v=13m9ZCB8gjw
# recursive soln https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65245/Iterative-Solutions-in-PythonC%2B%2B

## TC: O(N)
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # return the node if find the target
    # return node if encounter else return None
    # return current node if left and right are not None
    if not root: return root
    if root == p or root == q:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right

# concise
def lowestCommonAncestor2(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root or root == p or root == q:
        return root
    L = lowestCommonAncestor2(root.left, p, q)
    R = lowestCommonAncestor2(root.right, p ,q)
    return root if L and R else L or R