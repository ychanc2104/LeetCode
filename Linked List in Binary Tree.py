# https://leetcode.com/problems/linked-list-in-binary-tree/
# https://leetcode.com/problems/linked-list-in-binary-tree/solutions/524881/python-recursive-solution-o-n-l-time/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# first thought, TC:O(M*min(N,logM)), SC:O(N + logM) for recursive depth, N is size of head, M is size of root
def isSubPath(head, root) -> bool:
    def helper(head, root):  # check if is same
        if not head:
            return True
        if not root:
            return False
        return head.val == root.val and (helper(head.next, root.left) or helper(head.next, root.right))

    return root and (helper(head, root) or isSubPath(head, root.left) or isSubPath(head, root.right))

# KMP, TC:O(M+N), SC:O(logM)
def isSubPath2(head, root) -> bool:
    def convertLLToArray(head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

    def findLps(pattern):  # string --> [int]
        lps = [0] * (len(pattern))
        i = 0
        for j in range(1, len(pattern)):
            while i > 0 and pattern[j] != pattern[i]:
                i = lps[i - 1] # from prev repeating position,
            i += (pattern[j] == pattern[i]) # add one step
            lps[j] = i
        return lps
    pattern = convertLLToArray(head)
    lps = findLps(pattern)

    def dfs(root,i):
        if i == len(pattern) :
            return True
        if not root :
            return False
        # KMP search start -
        while i > 0 and root.val != pattern[i]:
            i = lps[i - 1]
        if root.val == pattern[i]:
            i += 1
        # kmp end
        return dfs(root.left,i) or dfs(root.right,i)

    return dfs(root,0)

# concise KMP, TC:O(M+N), SC:O(logM)
def isSubPath3(head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
    pattern = [head.val]
    lps = [0]
    i = 0
    head = head.next
    while head:
        while i > 0 and pattern[i] != head.val:
            i = lps[i-1]
        i += pattern[i]==head.val
        lps.append(i)
        pattern.append(head.val)
        head = head.next

    def dfs(root,i):
        if i == len(pattern):
            return True
        if not root:
            return False
        # KMP search start -
        while i > 0 and root.val != pattern[i]:
            i = lps[i - 1]
        i += root.val == pattern[i]
        # kmp end
        return dfs(root.left,i) or dfs(root.right,i)

    return dfs(root,0)



def findLps(pattern):  # string --> [int]
    lps = [0] * (len(pattern))
    i = 0
    for j in range(1, len(pattern)):
        print(j,i)
        while i > 0 and pattern[j] != pattern[i]: # move to previous matching position until matching
            i = lps[i - 1] # to prev position
        i += (pattern[j] == pattern[i]) # add one step
        lps[j] = i
    return lps


lps = findLps('abaabaacabcc')