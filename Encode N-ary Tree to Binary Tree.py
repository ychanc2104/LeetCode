# https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/description/



# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        # put children in its own leftmost
        if not root:
            return root
        bin_root = dummy = TreeNode(root.val)
        if not root.children:
            return bin_root
        n = len(root.children)
        bin_root.left = self.encode(root.children[0]) # put first children in the left
        bin_root = bin_root.left
        for i in range(1, n): # put siblings in the right
            bin_root.right = self.encode(root.children[i])
            bin_root = bin_root.right

        return dummy

    # Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        if not data:
            return data
        root = Node(data.val, [])
        data = data.left
        while data:
            root.children.append(self.decode(data))
            data = data.right
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))