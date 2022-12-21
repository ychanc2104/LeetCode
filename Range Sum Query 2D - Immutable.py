# https://leetcode.com/problems/range-sum-query-2d-immutable/description/


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n, m = len(matrix), len(matrix[0])
        self.prefix = [[0]*m for _ in range(n)]
        for i in range(n):
            s = 0
            for j in range(m):
                s += matrix[i][j]
                self.prefix[i][j] += s
                if i > 0:
                    self.prefix[i][j] += self.prefix[i-1][j]
        # print(self.prefix)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # prefix sum, prefix[i][j]: sum to row i and sum to j
        res = self.prefix[row2][col2]
        res -= self.prefix[row1-1][col2] if row1 > 0 else 0 # upper
        res -= self.prefix[row2][col1-1] if col1 > 0 else 0 # left
        res += self.prefix[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0 # overlap
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)