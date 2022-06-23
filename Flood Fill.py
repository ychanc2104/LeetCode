# https://leetcode.com/problems/flood-fill/


# first thought, TC: O(n)
def floodFill(image, sr: int, sc: int, color: int):
    visit = set()
    target = image[sr][sc]
    def dfs(r, c):
        if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]) or image[r][c] != target or (r, c) in visit:
            return
        image[r][c] = color
        visit.add((r, c))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # loop for four directions
        for (dx, dy) in directions:
            dfs(r + dy, c + dx)
    dfs(sr, sc)
    return image