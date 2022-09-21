# https://leetcode.com/problems/sudoku-solver/
# https://leetcode.com/problems/sudoku-solver/discuss/140837/Python-very-simple-backtracking-solution-using-dictionaries-and-queue-~100-ms-beats-~90

import collections

# backtracking + dfs, TC:O((9!)^9) each row, col or box of first grid with 9 choices and then 8,7,6,...1. There are 9 cols, rows or boxes in total., SC:O(81)
def solveSudoku(board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    row_set = collections.defaultdict(set)
    col_set = collections.defaultdict(set)
    box_set = collections.defaultdict(set)
    to_visit = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            value = board[i][j]
            if value != ".":
                row_set[i].add(value)
                col_set[j].add(value)
                box_set[(i // 3, j // 3)].add(value)
            else:
                to_visit.append((i, j))

    # print(to_visit)
    def dfs():
        if not to_visit:
            # no need to fill
            return True
        r, c = to_visit[-1]
        for v in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            if v in row_set[r] or v in col_set[c] or v in box_set[(r // 3, c // 3)]:
                continue
            # fill v into board
            to_visit.pop()
            board[r][c] = v
            row_set[r].add(v)
            col_set[c].add(v)
            box_set[(r // 3, c // 3)].add(v)
            # go depth, next grid
            if dfs():
                # stop when no element to visit
                return True
            # backtrack
            to_visit.append((r, c))
            board[r][c] = '.'
            row_set[r].remove(v)
            col_set[c].remove(v)
            box_set[(r // 3, c // 3)].remove(v)
        # no valid value can be added
        return False

    dfs()


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

solveSudoku(board)