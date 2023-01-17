# https://leetcode.com/problems/range-sum-query-mutable/description/
# https://leetcode.com/problems/range-sum-query-mutable/solutions/649011/python-recursive-segment-tree-approach/?languageTags=python
# https://leetcode.com/problems/range-sum-query-mutable/solutions/75730/148ms-python-solution-binary-indexed-tree/
# https://yuanchieh.page/posts/2022/2022-05-23-%E7%AE%97%E6%B3%95segment-tree-%E8%88%87-binary-indexed-tree-%E8%A7%A3%E9%A1%8C%E6%95%B4%E7%90%86/


import collections

# segment tree
class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = collections.defaultdict(int)
        self.low = 0
        self.high = len(nums) - 1
        self.createTree(nums, self.low, self.high)

    def createTree(self, nums, low, high, pos=0):
        if low == high:
            self.tree[pos] = nums[low]
            return nums[low]
        mid = (low + high) // 2
        L = self.createTree(nums, low, mid, 2 * pos + 1)  # to left
        R = self.createTree(nums, mid + 1, high, 2 * pos + 2)  # to right
        self.tree[pos] = L + R
        return L + R

    def rangeSum(self, qlow, qhigh, low, high, pos):
        # not overlapping
        if qlow > high or qhigh < low:
            return 0
        # fully overlapping
        if qlow <= low <= high <= qhigh:
            return self.tree[pos]
        # others
        mid = (low + high) // 2
        L = self.rangeSum(qlow, qhigh, low, mid, 2 * pos + 1)  # to left
        R = self.rangeSum(qlow, qhigh, mid + 1, high, 2 * pos + 2)  # to right
        return L + R

    def updatePoint(self, pos, low, high, i, val):
        if low == high:  # meet point
            self.tree[pos] = val
        else:
            # go depth
            mid = (low + high) // 2
            if i <= mid:  # go left
                self.updatePoint(2 * pos + 1, low, mid, i, val)
            else:  # go right
                self.updatePoint(2 * pos + 2, mid + 1, high, i, val)
            self.tree[pos] = self.tree[2 * pos + 1] + self.tree[2 * pos + 2]  # left + right
    # TC:O(logN)
    def update(self, index: int, val: int) -> None:
        self.updatePoint(0, self.low, self.high, index, val)
    # TC:O(logN)
    def sumRange(self, left: int, right: int) -> int:
        return self.rangeSum(left, right, self.low, self.high, 0)


# binary indexed tree
class NumArray2:

    def __init__(self, nums):
        self.n = len(nums)
        self.a, self.c = nums, [0] * (self.n + 1)
        # build BIT, TC:O(NlogN)
        for i in range(self.n):
            k = i + 1
            while k <= self.n:
                self.c[k] += nums[i] # prefix sum
                k += (k & -k) # 1, 1+1, 1+1+2, 1+1+2+4, adding leftmost bit
    # TC:O(logN)
    def update(self, i, val):
        diff, self.a[i] = val - self.a[i], val
        i += 1 # index in BIT
        while i <= self.n:
            self.c[i] += diff # update every node
            i += (i & -i)
    # TC:O(logN)
    def sumRange(self, i, j):
        res, j = 0, j + 1
        while j:
            res += self.c[j]
            j -= (j & -j)
        while i:
            res -= self.c[i]
            i -= (i & -i)
        return res

# binary indexed tree
class NumArray3:

    def __init__(self, nums):
        self.nums = nums
        self.N = len(self.nums)
        self.tree = [0] * (self.N + 1)
        ## optimize initiate BIT in O(n)
        for j in range(1, self.N + 1):
            self.tree[j] += self.nums[j - 1]
            if (j + (j & (-j))) <= self.N:
                self.tree[j + (j & (-j))] += self.tree[j]

    def update(self, i, val):
        diff = val - self.nums[i]
        self.nums[i] = val
        i += 1
        while i <= self.N:
            self.tree[i] += diff
            i += (i & (-i))

    def sumRange(self, i, j):
        return self.getSum(j) - self.getSum(i - 1)

    def getSum(self, i):
        sm = 0
        i += 1
        while i > 0:
            sm += self.tree[i]
            i -= (i & (-i))
        return sm

# binary indexed tree
class NumArray4:

    # TC:O(N), SC:O(N)
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.BIT = [0] * (len(nums) + 1)
        for i in range(1, len(nums)+1):
            self.BIT[i] += nums[i-1]
            if i + (i&-i) <= len(nums):
                # BIT[1+1] += BIT[1], BIT[3+1] += BIT[3]
                self.BIT[i + (i&-i)] += self.BIT[i]
    # TC:O(logN)
    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        index += 1
        while index <= len(self.nums):
            self.BIT[index] += diff # update all affected arr
            index += (index & -index)

    # TC:O(logN)
    def sumRange(self, left: int, right: int) -> int:
        L = 0
        while left > 0:
            L += self.BIT[left]
            left -= (left&-left)
        R = 0
        right += 1
        while right > 0:
            R += self.BIT[right]
            right -= (right&-right)
        return R - L


# Your NumArray object will be instantiated and called as such:
nums = [1,3,5]
obj = NumArray(nums)

param_2 = obj.sumRange(0,1)
# obj.update(1,2)
# param_3 = obj.sumRange(0,2)

# param_2 = obj.sumRange(left,right)


