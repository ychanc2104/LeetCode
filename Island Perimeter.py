# https://leetcode.com/problems/island-perimeter/description/


# count by surroundings, TC:O(NM), SC:O(1)
def islandPerimeter(grid: List[List[int]]) -> int:
    count = 0
    n, m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                count += 4
                if i > 0 and grid[i - 1][j] == 1:
                    count -= 1
                if i < n - 1 and grid[i + 1][j] == 1:
                    count -= 1
                if j > 0 and grid[i][j - 1] == 1:
                    count -= 1
                if j < m - 1 and grid[i][j + 1] == 1:
                    count -= 1
    return count


def islandPerimeter2(grid: List[List[int]]) -> int:
    count = 0
    n, m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                count += 4
                if i < n-1 and grid[i+1][j] == 1: # up
                    count -= 2
                if j > 0 and grid[i][j-1] == 1: # left
                    count -= 2
    return count