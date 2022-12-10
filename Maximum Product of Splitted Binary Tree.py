# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/


# first thought, two pass, TC:O(N), SC:O(logN)
def maxProduct(root: Optional[TreeNode]) -> int:
    def getSum(root):
        if not root: return 0
        return root.val + getSum(root.left) + getSum(root.right)

    s = getSum(root)
    res = [0]

    def helper(root):
        if not root: return 0
        left = helper(root.left)
        right = helper(root.right)
        res[0] = max(res[0], (s - right) * right, left * (s - left))
        return root.val + left + right

    helper(root)
    return res[0] % (10 ** 9 + 7)