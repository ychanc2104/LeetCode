# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)
    def insert(self, val):
        if val < self.val:
            if self.left==None:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)
        else:
            if self.right==None:
                self.right = TreeNode(val)
            else:
                self.right.insert(val)
    def print_tree(self):
        if self.left!=None:
            self.left.print_tree()
        else:
            print(self.val)
        if self.right!=None:
            self.right.print_tree()
        else:
            print(self.val)




# def build_binary_tree(data):
#     btree = TreeNode()
#     for i,d in enumerate(data):
#         if i==0:
#             btree.val = d
#         elif i<2**i:
#             btree.left = TreeNode(d)


btree = TreeNode(3)
btree.insert(9)
btree.insert(20)
# btree.insert(None)

data = [3,9,20,None,None,15,7]

