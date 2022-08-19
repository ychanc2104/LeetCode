# https://leetcode.com/problems/path-sum-iii/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# first thought, TC:O(N^2), SC:O(logN)
def pathSum(root, targetSum: int) -> int:
    res = [0]

    def helper(node, target):
        if not node: return
        # print(node.val, target)
        if target == node.val:
            # print(node.val, target)
            res[0] += 1
        # if not root.left and not root.right: return
        helper(node.left, target - node.val)
        helper(node.right, target - node.val)
        # root => left => right

    stack = []
    while stack or root:
        while root:
            helper(root, targetSum)
            stack.append(root)
            root = root.left
        root = stack.pop()
        root = root.right
    return res[0]

# use prefix sum, TC:O(N), SC:O(N), N for memo
def pathSum2(root, targetSum: int) -> int:
    res = [0]
    memo = {0: 1}

    def preorder(node, curSum):
        if not node: return
        curSum += node.val
        if curSum in memo:
            res[0] += memo.get(curSum, 0)
        memo[curSum + targetSum] = memo.get(curSum + targetSum, 0) + 1

        preorder(node.left, curSum)
        preorder(node.right, curSum)
        # remove curSum in memo to prevent using it during parallel subtree processing
        memo[curSum + targetSum] -= 1

    preorder(root, - targetSum)

    return res[0]