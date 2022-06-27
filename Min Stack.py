# https://leetcode.com/problems/min-stack/
# https://leetcode.com/problems/min-stack/discuss/49022/My-Python-solution

class MinStack:

    def __init__(self):
        self.stack = []

    # TC: O(1)
    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append((val, min(self.stack[-1][1], val)))
        else:
            self.stack.append((val, val))

    # TC: O(1)
    def pop(self) -> None:
        self.stack.pop()

    # TC: O(1)
    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    # TC: O(1)
    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
