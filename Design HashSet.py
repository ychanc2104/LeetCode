# https://leetcode.com/problems/design-hashset/description/


# use binary search, TC:O(logN) for each, SC:O(N)
class MyHashSet:

    def __init__(self):
        self.set = []

    def add(self, key: int) -> None:
        idx = self.bsearch(key)
        if idx == len(self.set) or self.set[idx] != key:
            self.set[idx:] = [key] + self.set[idx:]

    def remove(self, key: int) -> None:
        idx = self.bsearch(key)
        if idx == len(self.set) or self.set[idx] != key:
            return
        self.set[idx:] = self.set[idx + 1:]

    def contains(self, key: int) -> bool:
        idx = self.bsearch(key)
        if idx == len(self.set) or self.set[idx] != key:
            return False
        return True

    def bsearch(self, target):
        L, R = 0, len(self.set) - 1
        while L <= R:
            mid = (L + R) // 2
            if self.set[mid] == target:
                return mid
            if self.set[mid] > target:
                R = mid - 1
            else:
                L = mid + 1
        return L


# use binary search, TC:O(1) for each, SC:O(M)
class MyHashSet:

    def __init__(self):
        self.set = [False] * (10**6+1)

    def add(self, key: int) -> None:
        self.set[key] = True

    def remove(self, key: int) -> None:
        self.set[key] = False


    def contains(self, key: int) -> bool:
        return self.set[key]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)