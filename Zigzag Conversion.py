# https://leetcode.com/problems/zigzag-conversion/description/
# https://leetcode.com/problems/zigzag-conversion/solutions/3435/if-you-are-confused-with-zigzag-pattern-come-and-see/
# https://leetcode.com/problems/zigzag-conversion/solutions/3404/python-o-n-solution-in-96ms-99-43/


# reverse space and inverse by ~idx, TC:O(N), SC:O(N)
def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    res = []
    spaces = [2 * (numRows - 1 - i) for i in range(numRows)]
    spaces[-1] = 2 * (numRows - 1)
    # n = numRows
    for i in range(numRows):
        k = 0
        ps = i  # pointer in s
        idx = i  # pointer in spaces
        while ps < len(s):
            res.append(s[ps])
            ps += spaces[idx] if k % 2 == 0 else spaces[~idx]  # from the head or tail
            k += 1
    return ''.join(res)


# add to each row and reverse step when reach 0 or numRows-1, TC:O(N), SC:O(1)
def convert2(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    res = [[] for i in range(numRows)]
    idx = 0
    step = 1
    for char in s:
        res[idx].append(char)
        idx += step
        if idx == numRows-1 or idx == 0:
            step *= -1 # reverse step when reach end
    return ''.join([''.join(row) for row in res])