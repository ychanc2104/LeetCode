# https://leetcode.com/problems/n-queens/

# backtracking, TC:O(N!), SC:O(N^2)
def solveNQueens(n: int):
    # diagonal => (row - col) is constant
    # anti-diagonal => (row + col) is constant
    board = [['.'] * n for _ in range(n)]
    col_set = set()
    adia_set = set()
    dia_set = set()
    res = []

    def backtrack(r):
        # valid board
        if r == n:
            res.append([''.join(row) for row in board])
            return
            # each row with one queen
        # place queen from first column
        for col in range(n):
            # check next place
            if col in col_set or (r + col) in adia_set or (r - col) in dia_set:
                continue
            # place a queen
            board[r][col] = 'Q'
            col_set.add(col)
            adia_set.add(r + col)
            dia_set.add(r - col)

            backtrack(r + 1)
            # backtracking
            board[r][col] = '.'
            col_set.discard(col)
            adia_set.discard(r + col)
            dia_set.discard(r - col)

    backtrack(0)
    return res


res = solveNQueens(4)