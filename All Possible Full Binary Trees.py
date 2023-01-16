# https://leetcode.com/problems/all-possible-full-binary-trees/description/

import functools


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

# recursive, TC:O(2^n), SC:O(2^N)
def allPossibleFBT2(n: int) -> List[Optional[TreeNode]]:
    # 3:1, 5:2, 7:5
    @functools.lru_cache(None)
    def dfs(i): # full binary tree
        if i == 0:
            return [None]
        if i == 1:
            return [TreeNode(0)]
        if i % 2 == 0:
            return []
        res = []
        for j in range(1, i, 2): # i=1,3,5
            for left in dfs(i-j-1):
                for right in dfs(j):
                    res.append(TreeNode(0, left, right))
        return res
    # 5=> 1,1,3 1,3,1
    # 7=> 1,1,5(2) 1,3,3 1,5,1(2)
    return dfs(n) 