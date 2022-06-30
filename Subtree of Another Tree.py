# https://leetcode.com/problems/subtree-of-another-tree/
# Merkle hashing, https://leetcode.com/problems/subtree-of-another-tree/discuss/102741/Python-Straightforward-with-Explanation-(O(ST)-and-O(S%2BT)-approaches)




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # TC: O(N*T), N:number of nodes in root, T:number of nodes in subRoot
    def isSubtree(self, root, subRoot) -> bool:
        ## check if the same tree, TC: O(min(Np,Nq))
        def sameTree(p, q):
            if not p and not q:
                return True
            elif p and q and p.val==q.val:
                return sameTree(p.left, q.left) and sameTree(p.right, q.right)
            else:
                return False
        if not subRoot: return True
        if not root: return False
        if sameTree(root, subRoot):
            return True
        else:
            # recursively check the rest of tree
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # O(|s| + |t|) (Merkle hashing)
    def isSubtree2(self, s, t):
        from hashlib import sha256
        def hash_(x):
            S = sha256()
            S.update(bytes(x, encoding='utf-8'))
            return S.hexdigest()
        def merkle(node):
            if not node:
                return '#'
            m_left = merkle(node.left)
            m_right = merkle(node.right)
            node.merkle = hash_(m_left + str(node.val) + m_right)
            return node.merkle
        merkle(s)
        merkle(t)
        def dfs(node):
            if not node:
                return False
            return (node.merkle == t.merkle or
                    dfs(node.left) or dfs(node.right))
        return dfs(s)
    # O(|s| + |t|) (Merkle hashing)
    def isSubtree3(self, s, t):
        def hashify(node):
            if not node:
                return None
            key = (node.val, hashify(node.left), hashify(node.right))
            return memo.setdefault(key, len(memo))
        memo = {}
        hashify(s)
        return (t.val, hashify(t.left), hashify(t.right)) in memo

    def isSubtree4(self, root, subRoot) -> bool:

        def isSameTree(p, q):
            if p and q and p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            elif not p and not q:
                return True
            else:
                return False

        if root and subRoot:
            if root.val == subRoot.val and isSameTree(root, subRoot):
                return True
            else:
                return self.isSubtree4(root.left, subRoot) or self.isSubtree4(root.right, subRoot)
        else:
            return False

    # convert to string
    def isSubtree5(self, root, subRoot) -> bool:
        # ^4#^1#$$^2#$$([4,1,2])  ^3#^4#^1#$$^2#$$^5#$$ ([3,4,5,1,2])
        # $ for None,
        def convert(p):
            return "^" + str(p.val) + "#" + convert(p.left) + convert(p.right) if p else "$"
        s = convert(subRoot)
        r = convert(root)
        print(s, r)
        return s in r