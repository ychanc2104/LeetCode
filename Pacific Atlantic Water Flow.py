# https://leetcode.com/problems/pacific-atlantic-water-flow/
# https://leetcode.com/problems/pacific-atlantic-water-flow/discuss/1126937/Pacific-Atlantic-Water-Flow-or-Short-and-Easy-w-Explanation-and-diagrams

## neetcode solution, TC: O(MN), SC: O(MN)
# traverse all pos
def pacificAtlantic(heights):
    # find coordinates which flows to 4 edges
    pac = set()
    atl = set()
    rows = len(heights)
    cols = len(heights[0])

    def dfs(r, c, visit, pre):
        if (r, c) in visit:
            return
        if r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < pre:
            return
        visit.add((r, c))
        dfs(r - 1, c, visit, heights[r][c])
        dfs(r + 1, c, visit, heights[r][c])
        dfs(r, c - 1, visit, heights[r][c])
        dfs(r, c + 1, visit, heights[r][c])

    # run top and bottom for leftmost and rightmost
    for i in range(rows):
        dfs(i, 0, pac, heights[i][0])
        dfs(i, cols - 1, atl, heights[i][cols - 1])
    # run left and right for top and bottom
    for j in range(cols):
        dfs(0, j, pac, heights[0][j])
        dfs(rows - 1, j, atl, heights[rows - 1][j])

    return set.intersection(pac, atl)

def pacificAtlantic2(heights):
    n = len(heights)
    m = len(heights[0])
    def dfs(init, i, j, visit):
        if (i, j) in visit:
            return
        if i < 0 or j < 0 or i >= n or j >= m or heights[i][j] < heights[init[0]][init[1]]:
            return
        visit.add((i, j))
        for x, y in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            dfs((i, j), i + y, j + x, visit)
    # to pacific
    res_pac = set()
    # to atlantic
    res_atl = set()
    # adding the position which can flow to four sides
    for i in range(len(heights)):
        # flow to pac
        dfs((i, 0), i, 0, res_pac)
        # flow to atl
        dfs((i, m - 1), i, m - 1, res_atl)
    for j in range(len(heights[0])):
        # flow to pac
        dfs((0, j), 0, j, res_pac)
        # flow to atl
        dfs((n - 1, j), n - 1, j, res_atl)
    # print(res_pac, res_atl)
    return set.intersection(res_pac, res_atl)

# dfs
def pacificAtlantic3(heights: List[List[int]]) -> List[List[int]]:
    n, m = len(heights), len(heights[0])
    # use intersetion of two oceans
    # spread from edges
    stack_pac = []
    stack_atl = []
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                stack_pac.append((i, j))
            if i == n - 1 or j == m - 1:
                stack_atl.append((i, j))
    set_pac = set(stack_pac)  # dfs
    while stack_pac:
        r, c = stack_pac.pop()
        height_cur = heights[r][c]
        # explore four directions
        for ro, co in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            rn, cn = r + ro, c + co
            if rn < 0 or cn < 0 or rn >= n or cn >= m or (rn, cn) in set_pac or height_cur > heights[rn][cn]:
                continue
            stack_pac.append((rn, cn))
            set_pac.add((rn, cn))

    set_atl = set(stack_atl)
    while stack_atl:
        r, c = stack_atl.pop()
        height_cur = heights[r][c]
        # explore four directions
        for ro, co in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            rn, cn = r + ro, c + co
            if rn < 0 or cn < 0 or rn >= n or cn >= m or (rn, cn) in set_atl or height_cur > heights[rn][cn]:
                continue
            stack_atl.append((rn, cn))
            set_atl.add((rn, cn))
    return set_pac.intersection(set_atl)

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# find coordinates which flows to 4 edges

res = pacificAtlantic(heights)
res2 = pacificAtlantic2(heights)
