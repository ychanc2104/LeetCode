# https://leetcode.com/problems/set-matrix-zeroes/


## first though, SC: O(m+n)
def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    row = set()
    col = set()
    n, m = len(matrix), len(matrix[0])
    for i in range(n):
        for j in range(m):
            num = matrix[i][j]
            if num == 0:
                row.add(i)
                col.add(j)
    for r in row:
        matrix[r] = [0] * m
    for c in col:
        for k in range(n):
            matrix[k][c] = 0



    ## SC: O(1)
def setZeroes2(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """

    n, m = len(matrix), len(matrix[0])
    extra_store = False
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                if i == 0:
                    extra_store = True
                else:
                    matrix[i][0] = 0
                matrix[0][j] = 0
    # print(matrix, extra_store)
    # first to check first col
    for j in range(n):
        if matrix[j][0] == 0 and j != 0:
            matrix[j] = [0] * m

    # second to check first row
    for i, num in enumerate(matrix[0]):
        if num == 0:
            # make all col zero
            for j in range(n):
                matrix[j][i] = 0
    # final to check
    if extra_store:
        matrix[0] = [0] * m

# TC:O(M*N), SC:O(M+N)
def setZeroes3(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    # store zero position in rows and cols
    n = len(matrix)
    m = len(matrix[0])
    rows = [False] * n
    cols = [False] * m
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                rows[i] = True
                cols[j] = True

    # row
    for i in range(n):
        if rows[i]:
            matrix[i] = [0] * m
    # col
    for j in range(m):
        if cols[j]:
            for i in range(n):
                matrix[i][j] = 0


# store into matrix first row and col ,TC:O(M*N), SC:O(1)
def setZeroes4(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    # store zero position in rows and cols
    n = len(matrix)
    m = len(matrix[0])
    extra = False # store for first col
    # rows = [False] * n
    # cols = [False] * m
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                #matrix[0][j] = 0
                if j==0:
                    extra = True
                elif j > 0:
                    matrix[0][j] = 0
    # col
    for j in range(1,m):
        if matrix[0][j] == 0:
            for i in range(n):
                matrix[i][j] = 0
    # row
    for i in range(n):
        if matrix[i][0] == 0:
            matrix[i] = [0] * m
    # extra
    if extra:
        for i in range(n):
            matrix[i][0] = 0