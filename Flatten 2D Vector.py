# https://leetcode.com/problems/flatten-2d-vector/


class Vector2D:

    # TC:O(NM), SC:O(NM)
    def __init__(self, vec: List[List[int]]):
        self.vec= []
        for v in vec:
            for num in v:
                self.vec.append(num)
        self.i = 0

    # TC:O(1), SC:O(1)
    def next(self) -> int:
        val = self.vec[self.i]
        self.i += 1
        return val

    # TC:O(1), SC:O(1)
    def hasNext(self) -> bool:
        return self.i < len(self.vec)


# do not use extra space(better)
class Vector2D2:

    # TC:O(N) N is size of vec, SC:O(1)
    def __init__(self, vec: List[List[int]]):
        self.vec = vec  # original DS
        self.i = 0  # outer, make i always is valid, do not point to empty list
        self.j = 0  # inner
        while self.i < len(self.vec) and self.j >= len(self.vec[self.i]):
            self.i += 1

    # TC:O(N), SC:O(1)
    def next(self) -> int:
        if self.j < len(self.vec[self.i]):
            val = self.vec[self.i][self.j]
            self.j += 1
        # move to valid outer pointer
        while self.i < len(self.vec) and self.j >= len(self.vec[self.i]):
            self.i += 1
            self.j = 0
        return val

    # TC:O(1), SC:O(1)
    def hasNext(self) -> bool:
        return self.i < len(self.vec) and self.j < len(self.vec[self.i])

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()