# https://leetcode.com/problems/balanced-binary-tree/
# https://leetcode.com/problems/balanced-binary-tree/discuss/981648/Python-simple-dfs-explained
# https://leetcode.com/problems/balanced-binary-tree/discuss/35708/VERY-SIMPLE-Python-solutions-(iterative-and-recursive)-both-beat-90


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# first thought, dfs, slow
class Solution:
    def isBalanced(self, root) -> bool:
        self.res = True
        if not root:
            return True
        def dfs(root, count):
            if root:
                left = dfs(root.left, count+1)
                right = dfs(root.right, count+1)
                self.res = self.res and -1<=left-right<=1
                if self.res:
                    return max(left, right)
                else:
                    return count+1
            else:
                return count
        dfs(root, 0)
        return self.res

# dfs
class Solution2:
    def isBalanced(self, root) -> bool:
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if -1<=(left - right)<=1 and left!=-1 and right!=-1:
                return max(left, right) + 1
            else:
                return -1
        return dfs(root)!=-1


# tc: O(N), sc:O(h), h is height of tree
class Solution3:
    def isBalanced(self, root):
        self.res = True
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if left==-1 or right==-1 or abs(left-right)>1:
                self.res = False
            return max(left, right) + 1
        dfs(root)
        return self.res