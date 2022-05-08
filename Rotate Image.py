## https://leetcode.com/problems/rotate-image/
##　https://leetcode.com/problems/rotate-image/discuss/18884/Seven-Short-Solutions-(1-to-7-lines)

class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # row
        ## transpose
        for i in range(n):
            # col
            for j in range(n):
                if j>i:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        ## exchange left and right
        #row
        for i in range(n):
            #col
            for j in range(n):
                if j<n-j-1:
                    matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]

    def rotate2(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        ## exchange up and down
        for i in range(n // 2):
            matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]

        ## transpose
        # row
        for i in range(n):
            # col
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def rotate3(self, matrix):
        # reverse
        l = 0
        r = len(matrix) - 1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1
        # transpose
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


    def rotate4(self, matrix):
        """
        The most pythonic solution is a simple one-liner using [::-1] to flip the matrix upside down and then zip to transpose it. It assigns the result back into A, so it's "in-place" in a sense and the OJ accepts it as such, though some people might not.
        zip: a=[1,2,3], b=[4,5,6], c=[7,8,9], zip(a,b,c) => (1,4,7)
        :param matrix:
        :return:
        """
        matrix[:] = zip(*matrix[::-1])

## in-place
def rotate(matrix):
    matrix[:] = zip(*matrix[::-1])
    return matrix

## will create another matrix
def rotate2(matrix):
    matrix = zip(*matrix[::-1])
    return matrix


matrix = [[1,2,3],[4,5,6],[7,8,9]]


origin = matrix.copy()
A = rotate(matrix)
B = rotate2(matrix)