# https://leetcode.com/problems/search-a-2d-matrix/
# https://leetcode.com/problems/search-a-2d-matrix/solutions/487459/three-c-solutions-o-m-n-o-m-n-o-log-m-n/

# binary search, TC:O(logNM), N is number of rows, M is number of columns, SC:O(1)
def searchMatrix2(matrix, target: int) -> bool:
    # treat as 1D array and do binary search
    nrow = len(matrix)
    ncol = len(matrix[0])
    # print(i_row)
    L, R = 0, nrow * ncol - 1
    while L <= R:
        mid = L + (R - L) // 2
        row, col = mid // ncol, mid % ncol
        if matrix[row][col] > target:
            # move R to mid
            R = mid - 1
        elif matrix[row][col] < target:
            L = mid + 1
        else:
            return True
    return False


# saddleback search, TC:O(N+M), SC:O(1)
def searchMatrix2(matrix: List[List[int]], target: int) -> bool:
    # saddleback search
    m, n = len(matrix), len(matrix[0])
    r, c = 0, n-1
    while r < m and c >= 0:
        cell = matrix[r][c]
        if cell == target:
            return True
        elif cell < target:
            r += 1
        elif cell > target:
            c -= 1
    return False