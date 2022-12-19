# https://leetcode.com/problems/subtree-of-another-tree/
# Merkle hashing, https://leetcode.com/problems/subtree-of-another-tree/discuss/102741/Python-Straightforward-with-Explanation-(O(ST)-and-O(S%2BT)-approaches)




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# TC: O(N*T), N:number of nodes in root, T:number of nodes in subRoot
def isSubtree(root, subRoot) -> bool:
    ## check if the same tree, TC: O(min(Np,Nq))
    def sameTree(p, q):
        if not p and not q: return True
        if not p or not q: return False
        return p.val == q.val and sameTree(p.left, q.left) and sameTree(p.right, q.right)

    if not subRoot: return True
    if not root: return False
    return sameTree(root, subRoot) or isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


# O(|s| + |t|) (Merkle hashing)
def isSubtree2(s, t):
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
def isSubtree3(s, t):
    def hashify(node):
        if not node:
            return None
        key = (node.val, hashify(node.left), hashify(node.right))
        return memo.setdefault(key, len(memo))
    memo = {}
    hashify(s)
    return (t.val, hashify(t.left), hashify(t.right)) in memo

# convert to string
def isSubtree4(root, subRoot) -> bool:
    # ^4#^1#$$^2#$$([4,1,2])  ^3#^4#^1#$$^2#$$^5#$$ ([3,4,5,1,2])
    # $ for None,
    def convert(p):
        return "^" + str(p.val) + "#" + convert(p.left) + convert(p.right) if p else "$"
    s = convert(subRoot)
    r = convert(root)
    print(s, r)
    return s in r

# KMP, TC:O(N+M), SC:O(N+M)
def isSubtree5(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

    def convert(root, str_list):
        if not root:
            str_list.append('#')
            return
        # preorder
        str_list.append('^')  # prevent 12 and 2 case
        str_list.append(str(root.val))
        convert(root.left, str_list)
        convert(root.right, str_list)

    main_str_list, sub_str_list = [], []
    convert(root, main_str_list)
    convert(subRoot, sub_str_list)
    haystack = ''.join(main_str_list)
    needle = ''.join(sub_str_list)
    ## do KMP
    n, m = len(haystack), len(needle)
    # build cache
    dp = [0] * m
    i = 0
    for j in range(1, m):
        while i > 0 and needle[i] != needle[j]:
            i = dp[i - 1]
        i += needle[i] == needle[j]
        dp[j] = i

    # do search
    def dfs(ph=0, pn=0):
        if pn == m:
            return True
        if ph == n:
            return False
        while pn > 0 and needle[pn] != haystack[ph]:
            pn = dp[pn - 1]
        pn += needle[pn] == haystack[ph]
        return dfs(ph + 1, pn)
    return dfs()


needle = 'abcaacb'
haystack = 'asdgvvvasdabcbaab'

m = len(needle)
n = len(haystack)



# longest proper prefix which is also suffix
lps = [0] * m # failure function
# Length of Longest Border for prefix before it.
prev = 0
# Iterating from index-1. lps[0] will always be 0
i = 1

while i < m:
    if needle[i] == needle[prev]:
        # Length of Longest Border Increased
        prev += 1
        lps[i] = prev
        i += 1
    else:
        # Only empty border exist
        if prev == 0:
            lps[i] = 0
            i += 1
        # Try finding longest border for this i with reduced prev
        else:
            prev = lps[prev - 1]

# Pointer for haystack
haystack_pointer = 0
# Pointer for needle.
# Also indicates number of characters matched in current window.
needle_pointer = 0

while haystack_pointer < n:
    if haystack[haystack_pointer] == needle[needle_pointer]:
        # Matched Increment Both
        needle_pointer += 1
        haystack_pointer += 1
        # All characters matched
        if needle_pointer == m:
            print('success')
            break
            # return True
    else:
        if needle_pointer == 0:
            # Zero Matched
            haystack_pointer += 1
        else:
            # Optimally shift left needle_pointer.
            # Don't change haystack_pointer
            needle_pointer = lps[needle_pointer-1]