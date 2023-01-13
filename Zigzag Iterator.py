# https://leetcode.com/problems/zigzag-iterator/

import collections

# use queue
class ZigzagIterator:
    # TC:O(k), SC:O(k) k is number of vectors
    def __init__(self, v1: List[int], v2: List[int]):
        self.v = [v1, v2]
        self.queue = collections.deque()
        for i in range(len(self.v)):
            if self.v[i]:
                self.queue.append((i, 0)) # vector_index, element_index

    # TC:O(1)
    def next(self) -> int:
        i, k = self.queue.popleft()
        if k+1 < len(self.v[i]): # do not append next when exceed
            self.queue.append((i, k+1))
        return self.v[i][k]
    # TC:O(1)
    def hasNext(self) -> bool:
        return bool(self.queue)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())