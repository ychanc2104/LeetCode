# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/description/


# TC:O(NM), SC:O(NM)
def findRotation(mat: List[List[int]], target: List[List[int]]) -> bool:
    n, m = len(mat), len(mat[0])

    def rotate():
        mat[:] = list(zip(*mat))[::-1]

    def check():
        return all(mat[i][j] == target[i][j] for i in range(n) for j in range(m))

    for _ in range(4):
        if check():
            return True
        rotate()
    return False