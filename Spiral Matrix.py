# https://leetcode.com/problems/spiral-matrix/
# https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby

## continuously get first row and rotate counterclockwise 90 degrees (transpose => reverse)
## clockwise 90 degrees (reverse => transpose)

def spiralOrder(matrix):
    res = []
    while matrix:
        res.extend(matrix.pop(0))
        matrix[:] = list(zip(*matrix))[::-1]
    return res



def spiralOrder2(matrix):
    return matrix and [*matrix.pop(0)] + spiralOrder2([*zip(*matrix)][::-1])



def spiralOrder3(matrix):
    res = []
    if len(matrix) == 0:
        return res
    row_begin = 0
    col_begin = 0
    row_end = len(matrix) - 1
    col_end = len(matrix[0]) - 1
    while (row_begin <= row_end and col_begin <= col_end):
        for i in range(col_begin, col_end + 1):
            res.append(matrix[row_begin][i])
        row_begin += 1
        for i in range(row_begin, row_end + 1):
            res.append(matrix[i][col_end])
        col_end -= 1
        if (row_begin <= row_end):
            for i in range(col_end, col_begin - 1, -1):
                res.append(matrix[row_end][i])
            row_end -= 1
        if (col_begin <= col_end):
            for i in range(row_end, row_begin - 1, -1):
                res.append(matrix[i][col_begin])
            col_begin += 1
    return res

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

A = list(zip(*matrix))[::-1]


res = spiralOrder(matrix)