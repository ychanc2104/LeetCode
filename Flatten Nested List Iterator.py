# https://leetcode.com/problems/flatten-nested-list-iterator/
# https://leetcode.com/problems/flatten-nested-list-iterator/solutions/80142/8-line-python-solution/

import collections

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> [NestedInteger]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

class NestedIterator:
    # TC:O(N), SC:O(N)
    def __init__(self, nestedList: [NestedInteger]):
        self.flat = []

        def helper(data):
            for nested in data:
                if nested.isInteger():
                    self.flat.append(nested.getInteger())
                else:
                    helper(nested.getList())

        helper(nestedList)
        self.L = 0
        self.n = len(self.flat)

    # TC:O(1)
    def next(self) -> int:
        v = self.flat[self.L]
        self.L += 1
        return v

    # TC:O(1)
    def hasNext(self) -> bool:
        return self.L < self.n


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.queue = collections.deque(nestedList)

    def next(self) -> int:
        return self.queue.popleft().getInteger()

    def hasNext(self) -> bool:
        while self.queue:
            node = self.queue[0]
            if node.isInteger():  # True
                return True
            # is list
            # ex: x = [10,20] x.appendleft([1,2,3]) => x = [3,2,1,10,20]
            self.queue.extendleft(self.queue.popleft().getList()[::-1])  # append from idx-0 to leftmost
        return False



# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())