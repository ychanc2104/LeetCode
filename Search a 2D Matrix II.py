# https://leetcode.com/problems/search-a-2d-matrix-ii/description/

# binary search each rows, TC:O(NlogM), TC:O(1)
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    # binary search of each row
    def bsearch(nums, target):
        L, R = 0, len(nums) - 1
        while L <= R:
            mid = (L + R) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                R = mid - 1
            else:
                L = mid + 1
        return False

    for i in range(len(matrix)):
        if bsearch(matrix[i], target):
            return True
    return False

# linear search, TC:O(N+M), SC:O(1)
def searchMatrix2(matrix: List[List[int]], target: int) -> bool:
    # from top-right to bottom-left
    r, c = 0, len(matrix[0])-1
    while r < len(matrix) and c >= 0:
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] < target:
            r += 1
        elif matrix[r][c] > target:
            c -= 1
    return False