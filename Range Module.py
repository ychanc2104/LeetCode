# https://leetcode.com/problems/range-module/
# https://leetcode.com/problems/range-module/solutions/169353/ultra-concise-python-only-6-lines-of-actual-code-also-236ms-beats-100/
# https://leetcode.com/problems/range-module/solutions/495876/clean-and-concise-lazy-propagation-segment-tree/


import bisect

class RangeModule:

    def __init__(self):
        self.x = []  # 0,10,16,20

    # TC:O(logN)
    def addRange(self, left: int, right: int) -> None:
        # 0,10,16,20  add 10,16 => 0,25
        l1 = bisect.bisect_left(self.x, left)
        r1 = bisect.bisect_right(self.x, right)
        self.x[l1: r1] = [left] * (l1 % 2 == 0) + [right] * (r1 % 2 == 0)

    # TC:O(N), goal:O(logN)
    def queryRange(self, left: int, right: int) -> bool:
        # 10,14,16,20
        # print(self.x)
        l1 = bisect.bisect_right(self.x, left)
        r1 = bisect.bisect_left(self.x, right)
        return l1 == r1 and l1 % 2 and r1 % 2  # are odd(existing range) and locate at same position(range)

    # TC:O(N)
    def removeRange(self, left: int, right: int) -> None:
        # 0,20  remove 14,16 => 0,14,16,20  revmoe 12,18 => 0,12,18,20
        l1 = bisect.bisect_left(self.x, left)
        r1 = bisect.bisect_right(self.x, right)
        self.x[l1: r1] = [left] * (l1 % 2) + [right] * (r1 % 2)


class RangeModule2:

    def __init__(self):
        self.x = []  # 0,10,16,20

    def bsearch_left(self, nums, target):
        L, R = 0, len(nums) - 1
        while L <= R:
            mid = (L + R) // 2
            if nums[mid] >= target:
                R = mid - 1
            else:
                L = mid + 1
        return L  # leftmost [0,n]

    # TC:O(N) worst, insert used
    def addRange(self, left: int, right: int) -> None:
        # 0,10,16,20  add 10,16 => 0,25
        l1 = self.bsearch_left(self.x, left)
        r1 = self.bsearch_left(self.x, right + 1)
        self.x[l1: r1] = [left] * (l1 % 2 == 0) + [right] * (r1 % 2 == 0)

    # TC:O(logN)
    def queryRange(self, left: int, right: int) -> bool:
        # 10,14,16,20
        # print(self.x)
        l1 = self.bsearch_left(self.x, left + 1)
        r1 = self.bsearch_left(self.x, right)
        return l1 == r1 and l1 % 2 and r1 % 2  # are odd(existing range) and locate at same position(range)

    # TC:O(N), insert used
    def removeRange(self, left: int, right: int) -> None:
        # 0,20  remove 14,16 => 0,14,16,20  revmoe 12,18 => 0,12,18,20
        l1 = self.bsearch_left(self.x, left)
        r1 = self.bsearch_left(self.x, right + 1)
        self.x[l1: r1] = [left] * (l1 % 2) + [right] * (r1 % 2)

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)