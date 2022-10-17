# https://leetcode.com/problems/shortest-path-to-get-food/
# https://leetcode.com/problems/shortest-path-to-get-food/discuss/1027023/PythonC%2B%2B-clean-BFS-method-O(MN)


import collections
# TC: O(MN), SC:O(M+N)
def getFood(grid) -> int:
    # find '*'
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '*':
                pos = (i, j)
                break
                # BFS
    queue = [pos]
    step = 1
    while queue:
        leafs = []
        for r, c in queue:
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                # boundary check
                if r + y < 0 or c + x < 0 or r + y >= len(grid) or c + x >= len(grid[0]):
                    continue
                elif (grid[r + y][c + x] == 'O'):
                    # mark visited after checked
                    grid[r + y][c + x] = 'X'
                    leafs.append((r + y, c + x))
                elif grid[r + y][c + x] == '#':
                    return step
        queue = leafs
        step += 1
    return -1

# BFS, TC: O(MN), SC:O(M+N)
def getFood2(grid) -> int:
    # bfs
    # find person
    queue = collections.deque([])
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '*':
                queue.append(((i, j), 0))
                break

    while queue:
        (r, c), step = queue.popleft()
        # explore four directions
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 'X':
            continue
        if grid[r][c] == '#':
            return step
        grid[r][c] = 'X'
        for ro, co in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            rn, cn = r + ro, c + co
            queue.append(((rn, cn), step + 1))
    return -1