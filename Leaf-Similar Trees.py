# https://leetcode.com/problems/leaf-similar-trees/
# https://leetcode.com/problems/leaf-similar-trees/solutions/152329/c-java-python-o-h-space/

# first thought dfs, TC:O(N+M), SC:O(N+M)
def leafSimilar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    def dfs(root, res):
        if not root: return
        if not root.left and not root.right:
            res.append(root.val)
            return
        dfs(root.left, res)
        dfs(root.right, res)

    res1, res2 = [], []
    dfs(root1, res1)
    dfs(root2, res2)
    # print(res1, res2)
    return res1 == res2

# use yield to save memory dfs, TC:O(N+M), SC:O(logN+logM)
def leafSimilar2(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    def dfs(root):
        if not root: return
        if not root.left and not root.right:
            yield root.val
        for n in dfs(root.left):
            yield n
        for n in dfs(root.right):
            yield n

    return all(x == y for x, y in itertools.zip_longest(dfs(root1), dfs(root2)))

# concise, use yield to save memory dfs, TC:O(N+M), SC:O(logN+logM)
def leafSimilar3(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    def dfs(root):
        if not root: return
        if not root.left and not root.right:
            yield root.val
        yield from dfs(root.left)
        yield from dfs(root.right)
    return all(x==y for x,y in itertools.zip_longest(dfs(root1), dfs(root2)))