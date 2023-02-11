# https://leetcode.com/problems/design-excel-sum-formula/
# https://leetcode.com/problems/design-excel-sum-formula/solutions/104884/simple-elegant-python-solution/

class Excel:

    def __init__(self, height: int, width: str):
        self.width = ord(width) - ord('A') + 1
        self.height = height
        self.mat = [[0] * self.width for _ in range(height)]
        self.formulas = {}  # (r(int),c(str)):number(list)

    def set(self, row: int, column: str, val: int) -> None:
        self.formulas.pop((row, column), None)  # delete equation if exist
        self.mat[row - 1][ord(column) - ord('A')] = val

    def get(self, row: int, column: str) -> int:
        if (row, column) not in self.formulas:
            return self.mat[row - 1][ord(column) - ord('A')]  # no equations
        # parse formulas
        res = 0
        for area in self.formulas[(row, column)]:
            if ':' not in area:
                r, c = int(area[1:]), area[0]
                res += self.get(r, c)  # may be formula exist
            else:
                area1, area2 = area.split(':')
                r1, c1 = int(area1[1:]), area1[0]
                r2, c2 = int(area2[1:]), area2[0]
                for r in range(r1, r2 + 1):
                    for c in range(ord(c1) - ord('A'), ord(c2) - ord('A') + 1):
                        res += self.get(r, chr(c + ord('A')))  # may be formula exist
        return res

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        self.formulas[(row, column)] = numbers
        val = self.get(row, column)
        self.mat[row - 1][ord(column) - ord('A')] = val
        return val

# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)