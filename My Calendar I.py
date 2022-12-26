# https://leetcode.com/problems/my-calendar-i/description/
# https://leetcode.com/problems/my-calendar-i/solutions/109476/binary-search-tree-python/


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

