# https://leetcode.com/problems/construct-quad-tree/
# https://leetcode.com/problems/construct-quad-tree/solutions/195855/python-very-simple-recursive-solution-beats-97/



# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


# recursive, TC:O(N^2logN) for checking, SC:O(logN) for recursion depth
def construct(grid: List[List[int]]) -> 'Node':
    n = len(grid)

    def checkLeaf(i, j, l):
        for r in range(i, i + l):
            for c in range(j, j + l):
                if grid[i][j] != grid[r][c]:
                    return False
        return True

    def dfs(i, j, l):

        if i + l > n or j + l > n or checkLeaf(i, j, l):
            return Node(grid[i][j], 1, None, None, None, None)
        else:
            return Node(grid[i][j], 0,
                        dfs(i, j, l // 2), dfs(i, j + l // 2, l // 2),
                        dfs(i + l // 2, j, l // 2), dfs(i + l // 2, j + l // 2, l // 2))

    return dfs(0, 0, n)

# optimized recursive, TC:O(N^2) for checking, SC:O(logN) for recursion depth
def construct2(grid: List[List[int]]) -> 'Node':
    n = len(grid)

    def dfs(i, j, l):

        if l == 1:
            return Node(grid[i][j], 1, None, None, None, None)
        topLeft = dfs(i, j, l // 2)
        topRight = dfs(i, j + l // 2, l // 2)
        bottomLeft = dfs(i + l // 2, j, l // 2)
        bottomRight = dfs(i + l // 2, j + l // 2, l // 2)
        if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
            return topLeft
        return Node(grid[i][j], 0, topLeft, topRight, bottomLeft, bottomRight)

    return dfs(0, 0, n)