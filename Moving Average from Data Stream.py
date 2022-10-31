# https://leetcode.com/problems/moving-average-from-data-stream/description/

import collections

# Double-ended Queue, TC:O(1), SC:O(m), m is size
class MovingAverage:

    def __init__(self, size: int):
        self.window = size
        self.data_list = collections.deque([])
        self.mean = 0

    def next(self, val: int) -> float:
        n = len(self.data_list)
        if n < self.window:
            self.data_list.append(val)
            self.mean = (self.mean * n + val)/(n+1)
            return self.mean
        else: #
            prev = self.data_list.popleft() # O(1)
            self.data_list.append(val)
            self.mean = (self.mean * self.window + val - prev)/self.window
            return self.mean


# Circular Queue with Array
class MovingAverage2:
    def __init__(self, size: int):
        self.size = size
        self.queue = [0] * self.size
        self.head = self.window_sum = 0
        # number of elements seen so far
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.queue[tail] + val
        # move on to the next head
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val
        return self.window_sum / min(self.size, self.count)

# Circular Queue with Array
class MovingAverage3:

    def __init__(self, size: int):
        self.window = size
        self.data_list = []
        self.mean = 0
        self.head = 0

    def next(self, val: int) -> float:
        n = len(self.data_list)
        if n < self.window:
            self.data_list.append(val)
            self.mean = (self.mean * n + val)/(n+1)
            return self.mean
        else: #
            prev = self.data_list[self.head%self.window] # O(1)
            self.data_list[self.head%self.window] = val
            self.head += 1
            self.mean = (self.mean * self.window + val - prev)/self.window
            return self.mean



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)