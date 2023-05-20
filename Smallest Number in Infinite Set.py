# https://leetcode.com/problems/smallest-number-in-infinite-set/description/

import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.num = 1
        self.nums = [1]
        self.memo = set()

    def popSmallest(self) -> int:
        num = heapq.heappop(self.nums)
        if num == self.num:
            self.num += 1
            heapq.heappush(self.nums, self.num) # add next
            self.memo = set()
        else:
            self.memo.remove(num)
        return num

    def addBack(self, num: int) -> None:
        if self.num > num and num not in self.memo:
            # add back
            heapq.heappush(self.nums, num)
            self.memo.add(num)


class SmallestInfiniteSet2:

    def __init__(self):
        self.num = 1
        self.memo = set()

    def popSmallest(self) -> int:
        if self.memo:
            num = min(self.memo)
            self.memo.remove(num)
        else:
            num = self.num
            self.num += 1
        return num

    def addBack(self, num: int) -> None:
        if num < self.num:
            # add back
            self.memo.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)