# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/description/

import collections, random


# TC:O(1) for all
class RandomizedCollection:

    def __init__(self):
        self.data = []
        self.val2idx = collections.defaultdict(set)  # use set to speed up remove

    def insert(self, val: int) -> bool:
        self.data.append(val)
        self.val2idx[val].add(len(self.data) - 1)
        return len(self.val2idx[val]) == 1  #

    def remove(self, val: int) -> bool:
        # case: only one val
        if not self.val2idx[val]:
            return False

        idx = self.val2idx[val].pop()  # pop out smallest or randomly is ok
        val_last = self.data[-1]
        self.data[idx], self.data[-1] = self.data[-1], self.data[idx]  # swap to last
        self.val2idx[val_last].add(idx)
        self.val2idx[val_last].remove(len(self.data) - 1)  # remove biggest idx
        self.data.pop()  # remove
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()