# https://leetcode.com/problems/fancy-sequence/description/
# https://leetcode.com/problems/fancy-sequence/solutions/898753/python-time-o-1-for-each/
# https://leetcode.com/problems/fancy-sequence/solutions/981528/simple-o-1-with-explanation-beat-100-python/
# https://leetcode.com/problems/fancy-sequence/solutions/898861/c-math-solution-o-1-extra-space-and-o-1-time-for-each/

# TC:O(1) for all
class Fancy:
    def __init__(self):
        self.preSum = [0]
        self.preMul = [1]
        self.arr = []
        self.maxInt = 10**9 + 7

    def append(self, val: int) -> None:
        self.arr.append(val)
        self.preSum.append(self.preSum[-1])
        self.preMul.append(self.preMul[-1])

    def addAll(self, inc: int) -> None:
        self.preSum[-1] += inc

    def multAll(self, m: int) -> None:
        self.preSum[-1] = (self.preSum[-1] * m) % self.maxInt
        self.preMul[-1] = (self.preMul[-1] * m) % self.maxInt

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr): return -1
        ## Fermat's little theorem, a**p = a (mod p), p is a prime
        ## 1/self.preMul[idx] = pow(self.preMul[idx], self.maxInt-2) (mod self.maxInt)
        ## mul = (self.preMul[-1] // self.preMul[idx])
        mul = self.preMul[-1] * pow(self.preMul[idx], self.maxInt-2, self.maxInt)
        add = (self.preSum[-1] - mul * self.preSum[idx])
        res = self.arr[idx] * mul + add
        return res % self.maxInt



# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)