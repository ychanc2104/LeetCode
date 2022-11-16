# https://leetcode.com/problems/count-complete-tree-nodes/description/

# first thought,
def countNodes(root: Optional[TreeNode]) -> int:
    if not root: return 0
    # 0,1,2,3
    def dfs(root, i=0):
        if not root.left and not root.right:
            return 2 * i + 1  # left
        if not root.right:
            return 2 * i + 2  # right
        R = dfs(root.right, 2 * i + 2)
        L = dfs(root.left, 2 * i + 1)
        return min(R, L)
    return dfs(root)

# TC:O(N), SC:O(logN) for its height
def countNodes2(root: Optional[TreeNode]) -> int:
    return 1 + countNodes2(root.left) + countNodes2(root.right) if root else 0

# binary search, TC:O(logN*logN), SC:O(1)
def countNodes3(root: Optional[TreeNode]) -> int:
    def getHeight(root):
        h = 0
        while root.left:
            root = root.left
            h += 1
        return h
    def exist(root, h, i): # TC:O(logN)
        L, R = 0, 2**h - 1 # last level, ex: 0~7 0~3 and 4~7
        for _ in range(h):
            mid = (L + R) // 2
            if i > mid: # to right
                root = root.right
                L = mid # 3 or mid+1
            else:
                root = root.left
                R = mid # 3
        return root != None
    if not root: return 0
    h = getHeight(root)
    if h == 0: return 1
    L, R = 0, 2**h - 1
    while L <= R: # TC:O(logN)
        mid = (L + R) // 2
        if exist(root, h, mid): # to right
            L = mid + 1
        else:
            R = mid - 1
    return 2**h - 1 + L


# binary search and recursive call, TC:O(logN*logN), SC:O(1)
def countNodes4(root: Optional[TreeNode]) -> int:
    def getHeight(root):
        h = 0
        while root.left:
            root = root.left
            h += 1
        return h
    def exist(root, depth, i ,L, R):
        if depth == h:
            return True if root else False
        mid = (L + R)//2
        if i > mid: # to right
            return exist(root.right, depth+1, i, mid, R)
        else:
            return exist(root.left, depth+1, i, L, mid)
    if not root: return 0
    h = getHeight(root)
    if h == 0: return 1
    L, R = 0, 2**h - 1
    while L <= R: # TC:O(logN)
        mid = (L + R) // 2
        if exist(root, 0, mid, 0, 2**h - 1): # to right
            L = mid + 1
        else:
            R = mid - 1
    return 2**h - 1 + L

