# https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/
# https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/solutions/102275/python-simple-with-explanation/


# first thought, dp, TC:O(NM), SC:O(NM)
def longestLine(mat: List[List[int]]) -> int:
    # dp1(hor), dp2(ver), dp3(dia), dp4(anti-dia)

    res = 0
    n, m = len(mat), len(mat[0])
    dp1, dp2, dp3, dp4 = [[[0] * m for _ in range(n)] for _ in range(4)]
    for i in range(n):
        for j in range(m):
            cell = mat[i][j]
            if cell == 0: continue
            dp1[i][j] = (dp1[i][j - 1] + 1) if j > 0 else 1
            dp2[i][j] = (dp2[i - 1][j] + 1) if i > 0 else 1
            dp3[i][j] = (dp3[i - 1][j - 1] + 1) if i > 0 and j > 0 else 1
            dp4[i][j] = (dp4[i - 1][j + 1] + 1) if i > 0 and j + 1 < m else 1
            res = max(res, dp1[i][j], dp2[i][j], dp3[i][j], dp4[i][j])
    return res