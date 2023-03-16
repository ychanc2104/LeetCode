# https://leetcode.com/problems/game-of-life/description/


# first thought, TC:O(NM), SC:O(NM)
def gameOfLife(board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    m, n = len(board), len(board[0])
    counter = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for rn, cn in (
            (i + 1, j), (i, j + 1), (i + 1, j + 1), (i - 1, j), (i, j - 1), (i - 1, j - 1), (i - 1, j + 1),
            (i + 1, j - 1)):
                if not 0 <= rn < m or not 0 <= cn < n or not board[rn][cn]:
                    continue
                counter[i][j] += 1

    for i in range(m):
        for j in range(n):
            if board[i][j]:  # live cell
                if counter[i][j] < 2 or counter[i][j] > 3:
                    board[i][j] = 0
                elif counter[i][j] in [2, 3]:
                    continue
            else:
                if counter[i][j] == 3:
                    board[i][j] = 1

# TC:O(NM), SC:O(1)
def gameOfLife2(board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    m, n = len(board), len(board[0])
    for i in range(m):
        for j in range(n):
            counter = 0
            for rn, cn in (
            (i + 1, j), (i, j + 1), (i + 1, j + 1), (i - 1, j), (i, j - 1), (i - 1, j - 1), (i - 1, j + 1),
            (i + 1, j - 1)):
                if not 0 <= rn < m or not 0 <= cn < n:
                    continue
                if board[rn][cn] in [1, -1]:
                    counter += 1
            # -1 => live to dead, 2 => dead to live
            if board[i][j]:
                if counter < 2 or counter > 3:
                    board[i][j] = -1
            else:
                if counter == 3:
                    board[i][j] = 2

    for i in range(m):
        for j in range(n):
            if board[i][j] < 0:
                board[i][j] = 0
            elif board[i][j] > 1:
                board[i][j] = 1