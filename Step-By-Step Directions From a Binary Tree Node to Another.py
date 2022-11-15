# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/description/
# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/solutions/1612105/3-steps/

import collections

# first thought(TLE), TC:O(N), SC:O(N)
def getDirections(root: Optional[TreeNode], startValue: int, destValue: int) -> str:
    start, dest = [], []

    def appendUp(root, prev=None):
        if not root: return
        if root.val == startValue:
            start.append(root)
        if root.val == destValue:
            dest.append(root)
        root.up = prev
        appendUp(root.left, root)
        appendUp(root.right, root)

    appendUp(root)
    path = []
    queue = collections.deque([[start[0], path]])
    visited = set()
    while queue:
        node, path = queue.popleft()
        visited.add(node.val)
        if node.val == destValue:
            return ''.join(path)
        for n, s in ((node.up, 'U'), (node.left, 'L'), (node.right, 'R')):
            if not n or n.val in visited: continue
            queue.append([n, path + [s]])


# find LCA and do dfs, TC:O(N), SC:O(N)
def getDirections2(root: Optional[TreeNode], startValue: int, destValue: int) -> str:
    def getLCA(root):
        if not root or root.val == startValue or root.val == destValue:
            return root
        L = getLCA(root.left)
        R = getLCA(root.right)
        return root if L and R else L or R

    def dfs(root):
        if not root: return
        if root.val == startValue:
            res[0].extend(ps)
        elif root.val == destValue:
            res[1].extend(pd)
        ps.append('U')
        pd.append('L')
        dfs(root.left)
        ps.pop()
        pd.pop()
        ps.append('U')
        pd.append('R')
        dfs(root.right)
        ps.pop()
        pd.pop()

    LCA = getLCA(root)
    ps, pd = [], []
    res = [[], []]
    dfs(LCA)
    return ''.join(res[0]) + ''.join(res[1])

def getDirections3(root: Optional[TreeNode], startValue: int, destValue: int) -> str:
    def find(n: TreeNode, val: int, path: List[str]) -> bool:
        if n.val == val:
            return True
        if n.left and find(n.left, val, path):
            path += ["L"]
        elif n.right and find(n.right, val, path):
            path += ["R"]
        return path
    s, d = [], []
    find(root, startValue, s) # let all letter become 'U'
    find(root, destValue, d) # order is from bottom to top
    while len(s) and len(d) and s[-1] == d[-1]: # remove common prefix if in same side
        s.pop()
        d.pop()
    return "".join("U" * len(s)) + "".join(reversed(d))