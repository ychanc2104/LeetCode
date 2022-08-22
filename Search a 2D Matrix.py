# https://leetcode.com/problems/search-a-2d-matrix/


# binary search, TC:O(N+logM), N is number of rows, M is number of columns, SC:O(1)
def searchMatrix(matrix, target: int) -> bool:
    # find target row and do binary search
    i_row = 0
    nrow = len(matrix)
    #ncol = len(matrix[0])
    # TC:O(N)
    for i in range(1, nrow):
        if matrix[i_row][0] == target or matrix[i][0] == target:
            return True
        if matrix[i_row][0] < target <= matrix[i][0]:
            break
        else:
            i_row += 1
    # print(i_row)
    L, R = 0, len(matrix[i_row]) - 1
    while L <= R:
        mid = L + (R - L) // 2
        if matrix[i_row][mid] > target:
            # move R to mid
            R = mid - 1
        elif matrix[i_row][mid] < target:
            L = mid + 1
        else:
            return True
    return False

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
