# https://leetcode.com/problems/serialize-and-deserialize-bst/
# https://leetcode.com/problems/serialize-and-deserialize-bst/discuss/93224/Concise-iterative-Python-solution-using-stack-beat-99.
# https://leetcode.com/problems/serialize-and-deserialize-bst/solutions/93171/python-o-n-solution-easy-to-understand/


import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# use preorder
class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        # root => left => right, preorder
        res = []
        def dfs(root):
            if not root:
                res.append('#')
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ','.join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        # 0,1,2,3,4,5,6
        data_list = collections.deque(data.split(','))
        def helper():
            if not data_list:
                return None
            if data_list[0] == '#':
                data_list.popleft()
                return None
            root = TreeNode(int(data_list.popleft()))
            root.left = helper()
            root.right = helper()
            return root
        return helper()

# use BST property
class Codec2:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        # root => left => right, preorder
        res = []

        def dfs(root):
            if root:
                res.append(str(root.val))
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        return ','.join(res)

    # use BST property
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data: return None
        data_list = collections.deque(int(x) for x in data.split(','))

        def helper(MIN=float('-inf'), MAX=float('inf')):
            if not data_list or not MIN < data_list[0] < MAX:
                return None
            val = data_list.popleft()
            root = TreeNode(val)
            root.left = helper(MIN, val)
            root.right = helper(val, MAX)
            return root

        return helper()

class Codec3:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        # left => root => right, inorder
        # use preorder, root => left => right
        res = ''
        stack = []
        while stack or root:
            while root:
                res += f'{root.val},'
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return res[:-1]

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if data == '':
            return None
        nums = [int(num) for num in data.split(',')]
        root = node = TreeNode(nums[0])
        stack = []
        # root => left => right
        for num in nums[1:]:
            if num < node.val:
                node.left = TreeNode(num)
                stack.append(node)
                node = node.left
            else:
                # get root to assign right node
                while stack and stack[-1].val < num:
                    node = stack.pop()
                node.right = TreeNode(num)
                node = node.right
        return root


## use construct binary tree from preorder and inorder traversal
class Codec4:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        # left => root => right, inorder
        # use preorder, root => left => right
        res = ''
        stack = []
        while stack or root:
            while root:
                res += f'{root.val},'
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return res[:-1]

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """

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

        if data == '':
            return None
        preorder = [int(num) for num in data.split(',')]
        inorder = sorted(preorder)  # left=>root=>right
        root = buildTree(preorder, inorder)
        return root




# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans