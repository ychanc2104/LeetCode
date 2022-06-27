# https://leetcode.com/problems/implement-queue-using-stacks/
# https://leetcode.com/problems/implement-queue-using-stacks/discuss/64248/Clean-Python-Implementation-using-Two-Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/discuss/64284/Do-you-know-when-we-should-use-two-stacks-to-implement-a-queue

class MyQueue:

    # only use list.pop(), list.append()
    # SC: O(N)
    def __init__(self):
        self.input = []
        self.output = []

    # O(1)
    def push(self, x: int) -> None:
        self.input.append(x)
    # TC: amortized O(1)
    def pop(self) -> int:
        self.peek()
        return self.output.pop()
    # TC: amortized O(1)
    def peek(self) -> int:
        if not self.output:
            # pop to ouput
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
    # TC:O(1)
    def empty(self) -> bool:
        return self.output == self.input == []