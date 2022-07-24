# https://leetcode.com/problems/valid-sudoku/
# https://leetcode.com/problems/valid-sudoku/discuss/15451/A-readable-Python-solution

# first though, TC:O(n^2), SC:O(N)
def isValidSudoku(board) -> bool:
    row = len(board)
    col = len(board[0])
    # check rows
    for i in range(row):
        counter = set()
        for num in board[i]:
            if num == '.':
                continue
            if num not in counter:
                counter.add(num)
            else:
                # print(i, num, "false")
                return False
                # print("row ok")
    # check columns
    for i in range(col):
        counter = set()
        for j in range(row):
            if board[j][i] == '.':
                continue
            if board[j][i] not in counter:
                counter.add(board[j][i])
            else:
                return False
                # print("col ok")

    # check box
    for i in range(0, row, 3):
        for j in range(0, col, 3):
            counter = set()
            for k in range(i, i + 3):
                for m in range(j, j + 3):
                    if board[k][m] == '.':
                        continue
                    if board[k][m] not in counter:
                        counter.add(board[k][m])
                    else:
                        # print(i,j,k,m,board[k][m],counter, "false")
                        return False
    return True


def isValidSudoku2(board):
    def is_valid_row(board):
        for row in board:
            if not is_valid(row):
                return False
        return True

    def is_valid_column(board):
        for col in zip(*board):
            if not is_valid(col):
                return False
        return True

    def is_valid_square(board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3)
                          for y in range(j, j + 3)]
                if not is_valid(square):
                    return False
        return True

    def is_valid(value):
        res = [i for i in value if i != '.']
        return len(res) == len(set(res))

    return is_valid_row(board) and is_valid_column(board) and is_valid_square(board)