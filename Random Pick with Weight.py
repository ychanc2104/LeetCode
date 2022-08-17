# https://leetcode.com/problems/random-pick-with-weight/


import random

# linear search, TC:O(n), SC:O(n)
class Solution:

    def __init__(self, w: List[int]):
        total = sum(w)
        self.criteria = []
        cum = 0
        for e in w:
            cum += e/total
            self.criteria.append(cum)
        #print(self.criteria)

    def pickIndex(self) -> int:
        rand = random.random() # 0~1
        for i,c in enumerate(self.criteria):
            if rand <= c:
                return i





# leftmost binary search, TC:O(logn), SC:O(n)
class Solution2:

    def __init__(self, w: List[int]):
        total = sum(w)
        self.criteria = []
        cum = 0
        for e in w:
            cum += e/total
            self.criteria.append(cum)
        #print(self.criteria)

    def pickIndex(self) -> int:
        rand = random.random() # 0~1
        # binary search, find the first criteria which is greater and equal than rand
        # 0.1,0.3,0.6,0.9,1  rand=0.51, (L,R,mid) => (0,4,2), (0,1,0), (1,1,1), (2,1,x)
        # rand=0.7, (0,4,2), (3,4,3), (3,2,2)
        L, R = 0, len(self.criteria)-1
        while L <= R:
            mid = L + (R-L)//2
            if self.criteria[mid] > rand:
                # move R, go left
                R = mid - 1
            elif self.criteria[mid] == rand:
                return mid
            else:
                L = mid + 1
        return L

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()