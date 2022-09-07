# https://leetcode.com/problems/maximum-frequency-stack/

import collections


# TC:O(1) for all, SC:O(n)
class FreqStack:

    def __init__(self):
        self.stack = collections.defaultdict(list)
        self.counter = collections.Counter()
        self.maxfreq = 0  # index

    # TC:O(1)
    def push(self, val: int) -> None:
        # maintain max freq and counter
        self.counter[val] += 1
        f = self.counter[val]
        if f > self.maxfreq:
            self.maxfreq = f
        self.stack[f].append(val)

    # TC:O(1)
    def pop(self) -> int:
        # use a dict to store count of elements(count:list of val)
        val = self.stack[self.maxfreq].pop()
        self.counter[val] -= 1
        if len(self.stack[self.maxfreq]) == 0:
            self.maxfreq -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()