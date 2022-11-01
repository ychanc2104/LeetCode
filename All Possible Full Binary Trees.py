# https://leetcode.com/problems/all-possible-full-binary-trees/description/


#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive, TC:O(2^n), SC:O(2^N)
def allPossibleFBT(n: int) -> List[Optional[TreeNode]]:
    memo = {0:[], 1:[TreeNode(0)]}
    def helper(n):
        # 3 => root + dfs(1) + dfs(1)
        if not n&1: return []
        if n in memo: return memo[n]
        res = []
        for i in range(1,n,2): # iterate 2 by 2
            for left in helper(i): # deep copy
                for right in helper(n-1-i): # deep copy, minus 1 to count the root
                    res.append(TreeNode(0, left, right))
        memo[n] = res
        return memo[n]
    return helper(n)