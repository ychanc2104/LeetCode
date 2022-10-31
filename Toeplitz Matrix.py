# https://leetcode.com/problems/toeplitz-matrix/description/


# first thought, TC:O(M*N), SC:O(M+N) N is rows and M is columns
def isToeplitzMatrix(matrix: List[List[int]]) -> bool:
    memo = {}
    # diag: r-c is constant
    for c in range(len(matrix[0])):  # columns
        # rows
        for r in range(len(matrix)):
            if c - r not in memo:
                memo[c - r] = matrix[r][c]
            else:
                if matrix[r][c] != memo[c - r]:
                    return False
    return True


# pairing check and generator expression, TC:O(M*N), SC:O(1) N is rows and M is columns
def isToeplitzMatrix2(matrix: List[List[int]]) -> bool:
    return all(r==0 or c==0 or matrix[r-1][c-1]==matrix[r][c] for r in range(len(matrix)) for c in range(len(matrix[0])))