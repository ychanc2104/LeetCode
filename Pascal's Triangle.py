# https://leetcode.com/problems/pascals-triangle/description/

# TC:O(n^2), SC:O(n)
def generate(numRows: int) -> List[List[int]]:
    res = []
    for i in range(numRows): # O(n)
        temp = [1] * (i + 1)
        for j in range(1, i): # O(n)
            temp[j] = res[i - 1][j - 1] + res[i - 1][j]
        res.append(temp)
    return res