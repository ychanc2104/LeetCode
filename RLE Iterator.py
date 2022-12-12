# https://leetcode.com/problems/rle-iterator/description/

# binary search, TC:O(logN), SC:O(N)
class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.cum = [] # 3,3,5
        self.nums = [] # 8,9,5
        self.n = 0
        s = 0
        for i in range(0, len(encoding), 2): # 0,6,2  => 0,2,4
            s += encoding[i]
            self.cum.append(s)
            self.nums.append(encoding[i+1])

    def next(self, n: int) -> int:
        def bsearch(cum, target):
            L, R = 0, len(cum)-1
            while L <= R:
                mid = (L+R)//2
                if cum[mid] >= target:
                    R = mid - 1
                else:
                    L = mid + 1
            return L # [0, len(cum)]
        self.n += n
        idx = bsearch(self.cum, self.n)
        return self.nums[idx] if idx < len(self.cum) else -1