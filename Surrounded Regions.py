# https://leetcode.com/problems/surrounded-regions/description/


# first thought dfs, TC:O(NM), SC:O(NM)
def solve(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    n, m = len(board), len(board[0])

    def dfs(i, j):
        if i < 0 or i >= n or j < 0 or j >= m or board[i][j] == 'X' or (i, j) in visit: return False
        if i == 0 or j == 0 or i == n - 1 or j == m - 1: return True
        visit.add((i, j))
        path.add((i, j))
        res = False
        for ro, co in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            temp = dfs(i + ro, j + co)
            res = res or temp
        return res

    visit = set()
    filpped = set()
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0 or (i, j) in visit: continue
            path = set()
            if not dfs(i, j):  # not connect with edge
                filpped.update(path)
    # print(filpped)
    for i, j in filpped:
        board[i][j] = 'X'


# first thought dfs, TC:O(NM), SC:O(NM)
def solve(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    n, m = len(board), len(board[0])
    def dfs(i, j):
        # start from boarder and mark as E, E is escaped
        if i < 0 or i >= n or j < 0 or j >= m or board[i][j] != 'O': return
        board[i][j] = 'E'
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    # mark all 'O' connected with edges as 'E'
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0 or i == n-1 or j == m-1:
                dfs(i, j)
    # 'O' to 'X' and 'E' to 'O'
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'E':
                board[i][j] = 'O'