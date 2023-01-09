# https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/
# https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/solutions/68142/java-o-n-and-o-1-extra-space/


# use stack, TC:O(N), SC:O(N)
def verifyPreorder(preorder: List[int]) -> bool:
    # root=>left=>right
    n = len(preorder)
    stack = []  # put min in stack
    low = float('-inf')
    for i in range(n):
        if preorder[i] < low:  # right node should not be smaller than left node
            return False
        # cut valid node
        while stack and preorder[i] > stack[-1]:
            low = stack.pop()
        stack.append(preorder[i])
    return True

# store in-place, TC:O(N), SC:O(1)
def verifyPreorder2(preorder: List[int]) -> bool:

    # root=>left=>right
    n = len(preorder)
    low = float('-inf')
    i = 0
    for x in preorder:
        if x < low:  # right node should not be smaller than left node
            return False
        # cut valid node
        while i > 0 and x > preorder[i - 1]:
            low = preorder[i - 1]
            i -= 1
        preorder[i] = x
        i += 1
    return True