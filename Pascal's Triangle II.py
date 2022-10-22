# https://leetcode.com/problems/pascals-triangle-ii/description/


# first thought, dp, TC:O(n^2), SC:O(2n)
def getRow(rowIndex: int) -> List[int]:
    f0 = [1]
    for i in range(rowIndex + 1):
        f1 = [1] * (i + 1)
        for j in range(1, i):
            f1[j] = f0[j - 1] + f0[j]
        f0 = f1
    return f0

# memory saved dp, TC:O(n^2), SC:O(n)
def getRow2(rowIndex: int) -> List[int]:
    f0 = [1] * (rowIndex + 1)
    for i in range(rowIndex+1):
        for j in range(i-1,0,-1):
            f0[j] = f0[j-1] + f0[j]
    return f0

# math, TC:O(n), SC:O(1)
def getRow3(rowIndex: int) -> List[int]:
    up = rowIndex
    down = 1
    res = [1] * (rowIndex + 1)
    for i in range(1, rowIndex):
        res[i] = int(res[i - 1] * up / down)
        up -= 1
        down += 1
    return res