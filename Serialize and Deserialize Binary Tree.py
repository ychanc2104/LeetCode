# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/396124/Python-very-easy-to-understand-recursive-preorder-with-comments


import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    # DFS, preorder traversal, TC:O(N), SC:O(N)
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # preorder (root->left->right)
        if not root:
            return 'N'
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)

    # TC:O(N), SC:O(N)
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # return data

        preorder = collections.deque(data.split(','))
        def helper():
            if preorder[0] == 'N':
                preorder.popleft()
                return None
            root = TreeNode(int(preorder.popleft()))
            root.left = helper()
            root.right = helper()
            return root
        return helper()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))