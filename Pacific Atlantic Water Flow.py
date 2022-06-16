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





heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# find coordinates which flows to 4 edges
pac = set()
atl = set()
rows = len(heights)
cols = len(heights[0])

def dfs(r, c, visit, pre):
    if (r,c) in visit:
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
    dfs(rows-1, j, atl, heights[rows-1][j])

res = set.intersection(pac, atl)