# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# https://www.youtube.com/watch?v=13m9ZCB8gjw
# recursive soln https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65245/Iterative-Solutions-in-PythonC%2B%2B

## TC: O(N)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # return the node if find the target
        if not root:
            return None
        if root.val==p.val or root.val==q.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        else:
            return left if left else right