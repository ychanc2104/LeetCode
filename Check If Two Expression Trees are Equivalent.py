# https://leetcode.com/problems/check-if-two-expression-trees-are-equivalent/description/
# https://leetcode.com/problems/check-if-two-expression-trees-are-equivalent/solutions/884387/python-simple-dfs-solution-and-follow-up/?orderBy=most_votes


import collections

# first thought, count nodes, TC:O(N), SC:O(N)
def checkEquivalence(root1: 'Node', root2: 'Node') -> bool:
    def dfs(root):
        if not root:
            return collections.Counter()
        counter = collections.Counter(root.val)
        counter += dfs(root.left) + dfs(root.right)
        return counter

    return dfs(root1) == dfs(root2)

# count nodes, TC:O(N), SC:O(N)
def checkEquivalence2(root1: 'Node', root2: 'Node') -> bool:
    counter = [0] * 26

    def dfs(root, sign):
        if not root:
            return
        if root.val == '+':
            dfs(root.left, sign)
            dfs(root.right, sign)
        elif root.val == '-':  # follow-up
            dfs(root.left, sign)
            dfs(root.right, -sign)
        else:  # is digit
            counter[ord(root.val) - ord('a')] += sign

    dfs(root1, 1)
    dfs(root2, -1)
    return all(c == 0 for c in counter)



# follow-up, subtraction include, TC:O(N), SC:O(N)
def checkEquivalence3(root1: 'Node', root2: 'Node') -> bool:
    def dfs(root):
        if not root:
            return collections.Counter()
        counter = collections.Counter(root.val)
        counter += dfs(root.left)
        if root.val == '-':
            counter += -dfs(root.right)
        else:
            counter += dfs(root.right)
        return counter
    return dfs(root1) == dfs(root2)