# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree(TreeNode):
    def insert(self, val):
        if self.val!=None:
            if val <= self.val:
                if self.left==None:
                    self.left = BinarySearchTree(val)
                else:
                    self.left.insert(val)
            else:
                if self.right==None:
                    self.right = BinarySearchTree(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

    def __repr__(self):
        return f"node value is {self.val}"

    def print_tree_dfs(self):
        print(self.val)
        if self.left!=None:
            self.left.print_tree_dfs()
        if self.right!=None:
            self.right.print_tree_dfs()
    def print_tree_bfs(self):
        print("print all node by BFS")
        queue = [self]
        while queue!=[]:
            # print(temp)
            temp = queue.pop(0)
            print(temp.val)
            if temp.left!=None:
                queue.append(temp.left)
            if temp.right!=None:
                queue.append(temp.right)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        depth = 0
        if root == None:
            return depth
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right))+1



bst = BinarySearchTree()
data = [10,9,5,15,20,12]

for d in data:
    bst.insert(d)


max_depth = Solution().maxDepth(bst)
