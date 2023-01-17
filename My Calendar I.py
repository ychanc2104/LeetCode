# https://leetcode.com/problems/my-calendar-i/
# https://leetcode.com/problems/my-calendar-i/solutions/2113747/python-clean-segment-tree-solution/
# https://leetcode.com/problems/my-calendar-i/solutions/1363530/python-8-lines-array-segment-tree-with-explanation-beat-90/
# https://leetcode.com/problems/my-calendar-i/solutions/109476/binary-search-tree-python/

import collections


# segment tree, TLE
class Node:
    def __init__(self, start, end, left=None, right=None):
        self.start = start
        self.end = end
        self.left = left
        self.right = right

class MyCalendar:

    def __init__(self):
        self.root = None

    # TC:O(logN), SC:O(N)
    def book(self, start: int, end: int) -> bool:
        def helper(start, end, node):
            if end <= node.start:  # go left
                if not node.left:
                    node.left = Node(start, end)
                    return True
                return helper(start, end, node.left)
            elif start >= node.end:  # go right
                if not node.right:
                    node.right = Node(start, end)
                    return True
                return helper(start, end, node.right)
            return False  # do nothing

        if not self.root:
            self.root = Node(start, end)
            return True
        return helper(start, end, self.root)


# segment tree, TLE
class MyCalendar2:
    def __init__(self):
        self.tree = collections.defaultdict(bool)
        # already existing => True
    def check(self, qlow, qhigh, pos=0, low=0, high=10**9):
        # not overlapping
        if qlow > high or qhigh < low:
            return False # do nothing
        # total overlapping
        if qlow <= low <= high <= qhigh:
            return self.tree[pos]
        # go depth
        mid = (low + high)//2
        L = self.check(qlow, qhigh, 2*pos+1, low, mid)
        R = self.check(qlow, qhigh, 2*pos+2, mid+1, high)
        return L or R

    def update(self, qlow, qhigh, pos=0, low=0, high=10**9):
        # not overlapping
        if qlow > high or qhigh < low:
            return  # do nothing
        if low == high:
            self.tree[pos] = True # mark occupied
            return  # insert success
        # others
        mid = (low + high)//2
        L = self.update(qlow, qhigh, 2*pos+1, low, mid)
        R = self.update(qlow, qhigh, 2*pos+2, mid+1, high)
        self.tree[pos] = self.tree[2*pos+1] or self.tree[2*pos+2]

    def book(self, start: int, end: int) -> bool:
        if self.check(start, end-1): # True => already exist
            return False
        self.update(start, end-1)
        return True



from sortedcontainers import SortedList


class MyCalendar3:
    def __init__(self):
        self.calendar = SortedList()

    def book(self, start: int, end: int) -> bool:
        idx = self.calendar.bisect_right((start, end))
        if (idx > 0 and self.calendar[idx - 1][1] > start) or (
                idx < len(self.calendar) and self.calendar[idx][0] < end):
            return False
        self.calendar.add((start, end))
        return True


obj = MyCalendar()
param_1 = obj.book(0,3)
param_2 = obj.book(4,7)

param_3 = obj.book(1,5)