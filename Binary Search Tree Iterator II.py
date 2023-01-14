# https://leetcode.com/problems/binary-search-tree-iterator-ii/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# pre-calculating arr,
class BSTIterator:
    # TC:O(N), SC:O(N)
    def __init__(self, root: Optional[TreeNode]):
        # in-order, left=>root=>right, sorted order
        self.arr = []  # to store next
        self.dfs(root)
        self.i = -1

    # TC:O(1)
    def hasNext(self) -> bool:
        return self.i + 1 < len(self.arr)

    # TC:O(1)
    def next(self) -> int:
        self.i += 1
        val = self.arr[self.i]
        return val

    # TC:O(1)
    def hasPrev(self) -> bool:
        return self.i - 1 > 0

    # TC:O(1)
    def prev(self) -> int:
        self.i -= 1
        val = self.arr[self.i]
        return val

    def dfs(self, root):
        if not root:
            return

        self.dfs(root.left)
        self.arr.append(root.val)
        self.dfs(root.right)

# follow-up, do not pre-calculate
class BSTIterator2:

    def __init__(self, root: Optional[TreeNode]):
        # in-order, left=>root=>right, sorted order
        self.node = root
        self.stack = [] # to store node
        self.arr = [] # to store val
        self.i = -1

    def hasNext(self) -> bool:
        return (self.i+1 < len(self.arr)) or self.stack or self.node

    def next(self) -> int:
        if self.i+1 >= len(self.arr): # out of range
            node = self.node
            while node:
                self.stack.append(node)
                node = node.left
            node = self.stack.pop()
            self.node = node.right
            self.arr.append(node.val)
        self.i += 1
        val = self.arr[self.i]
        return val

    def hasPrev(self) -> bool:
        return self.i-1 >= 0

    def prev(self) -> int:
        self.i -= 1
        val = self.arr[self.i]
        return val







# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()