# https://leetcode.com/problems/inorder-successor-in-bst-ii/description/
# https://leetcode.com/problems/inorder-successor-in-bst-ii/solutions/401979/simple-python-solution/?orderBy=most_votes
# https://leetcode.com/problems/inorder-successor-in-bst-ii/solutions/921792/python-find-successor-without-looking-up-any-of-the-node-s-values/


# recursion, TC:O(logN), SC:O(logN)
def inorderSuccessor(node: 'Node') -> 'Optional[Node]':
    def dfs(root):
        if not root.right:  # must go up
            return findUp(root.parent)
        # must to down
        return findDown(root.right)

    def findUp(root):
        if not root:
            return None
        if root.val > node.val:
            return root
        return findUp(root.parent)  # go up until reach none

    def findDown(root):
        # if not root or not root.left or root.left.val <= node.val:
        #     return root
        ## or
        if not root.left: # current root is answer
            return root
        return findDown(root.left)

    return dfs(node)



# iterative, TC:O(logN), SC:O(1)
def inorderSuccessor(node: 'Node') -> 'Optional[Node]':
    # two cases, 1.right node not existing, 2.others
    if not node.right:
        while node.parent and node.parent.val <= node.val:
            node = node.parent
        return node.parent
    # go down
    node = node.right
    while node.left:
        node = node.left
    return node