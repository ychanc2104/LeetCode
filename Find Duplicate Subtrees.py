# https://leetcode.com/problems/find-duplicate-subtrees/description/
# https://leetcode.com/problems/find-duplicate-subtrees/solutions/106016/o-n-time-and-space-lots-of-analysis/?orderBy=most_votes

import collections


# postorder traversal, dfs and hashing, TC:O(N^2), N for traversal and N for hashing tuple, SC:O(N^2)
def findDuplicateSubtrees(root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    res = []
    counter = collections.defaultdict(int)

    def dfs(root):
        if not root:
            return ()
        root_tuple = (dfs(root.left), root.val, dfs(root.right))
        counter[root_tuple] += 1 # key is tuple, take O(N), N is length of tuple
        if counter[root_tuple] == 2:
            res.append(root)
        return root_tuple

    dfs(root)
    return res


# postorder traversal, dfs and hashing, TC:O(N), SC:O(N)
def findDuplicateSubtrees(root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

    res = []
    counter = collections.defaultdict(int)
    memo = {}
    def dfs(root):
        if not root:
            return 0
        root_tuple = (dfs(root.left), root.val, dfs(root.right))
        if root_tuple not in memo:
            memo[root_tuple] = len(memo) + 1
        counter[memo[root_tuple]] += 1
        if counter[memo[root_tuple]] == 2:
            res.append(root)
        return memo[root_tuple]
    dfs(root)
    return res