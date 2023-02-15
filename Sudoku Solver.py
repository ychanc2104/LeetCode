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

# backtracking + dfs, TC:O((9!)^9) each row, col or box of first grid with 9 choices and then 8,7,6,...1. There are 9 cols, rows or boxes in total., SC:O(81)
def solveSudoku2(board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    # box: 0-8, row: 0-8, col: 0-8
    box = collections.defaultdict(set)  # c//3+3r
    row = collections.defaultdict(set)  # r
    col = collections.defaultdict(set)  # c
    empty_cells = []
    for i in range(9):
        for j in range(9):
            cell = board[i][j]
            if cell == '.':
                empty_cells.append((i, j))
                continue
            row[i].add(cell)
            col[j].add(cell)
            box[j // 3 + 3 * (i // 3)].add(cell)

    # print(empty_cells)
    def backtrack():
        if not empty_cells:
            return

        r, c = empty_cells[-1]

        for i in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            if i in row[r] or i in col[c] or i in box[c // 3 + 3 * (r // 3)]:
                continue
            empty_cells.pop()
            board[r][c] = i
            row[r].add(i)
            col[c].add(i)
            box[c // 3 + 3 * (r // 3)].add(i)
            backtrack()
            if empty_cells:  # already filled all
                empty_cells.append((r, c))
                board[r][c] = '.'
                row[r].remove(i)
                col[c].remove(i)
                box[c // 3 + 3 * (r // 3)].remove(i)

    backtrack()