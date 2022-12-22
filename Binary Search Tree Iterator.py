# https://leetcode.com/problems/binary-search-tree-iterator/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# use stack
class BSTIterator:

    # TC:O(logN) for construction, SC:O(logN)
    def __init__(self, root: Optional[TreeNode]):
        # in-order, left=>root=>right
        self.stack = [] # max to store O(h) = O(logN)
        self.dfs(root)
    # TC: amortized O(1), SC:O(h)
    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self.dfs(node.right)
        return node.val
    # TC:O(1)
    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def dfs(self, root):
        if root:
            self.stack.append(root)
            self.dfs(root.left)

# use generator
class BSTIterator2:

    # TC:O(N) for construction, SC:O(1)
    def __init__(self, root: Optional[TreeNode]):
        # in-order, left=>root=>right
        self.stack = [] # size one
        def dfs(root):
            if root:
                yield from dfs(root.left)
                yield root
                yield from dfs(root.right)
        self.iterator = dfs(root)

    # TC:O(1), SC:O(1)
    def next(self) -> int:
        if self.stack:
            val = self.stack.pop().val
        else:
            val = next(self.iterator, TreeNode()).val
        return val

    # TC:O(1), SC:O(1)
    def hasNext(self) -> bool:
        if self.stack:
            return True
        node = next(self.iterator, None)
        if not node: return False
        self.stack.append(node)
        return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()