# https://leetcode.com/problems/sparse-matrix-multiplication/description/


# first thought, directly mul, TC:O(NMk), SC:O(1)
def multiply(mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
    m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
    res = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for t in range(k):
                res[i][j] += mat1[i][t] * mat2[t][j]
    return res




# store wisely, TC:O(NMk), SC:O(NM+Mk)
def multiply2(mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
    m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
    res = [[0] * n for _ in range(m)]

    # store non-zero elements efficiently
    def helper(mat):
        n, m = len(mat), len(mat[0])
        res = [[] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                cell = mat[i][j]
                if cell == 0: continue
                res[i].append([cell, j])  # val, col
        return res

    A, B = helper(mat1), helper(mat2)
    # print(A, B)
    for i in range(m):
        for va, ca in A[i]:
            for vb, cb in B[ca]:
                res[i][cb] += va * vb

    return res