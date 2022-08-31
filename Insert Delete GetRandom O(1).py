# https://leetcode.com/problems/insert-delete-getrandom-o1/

import random

# use list + hashtable, TC:O(1), SC:O(n)
class RandomizedSet:

    def __init__(self):
        self.rand_val_dict = {}  # val: index
        self.rand_list = []

    def insert(self, val: int) -> bool:
        if val in self.rand_val_dict:
            return False
        self.rand_val_dict[val] = len(self.rand_list)
        self.rand_list.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.rand_val_dict:
            return False
        index_remove = self.rand_val_dict[val]
        # swap val to the end
        self.rand_val_dict[self.rand_list[-1]] = index_remove
        self.rand_list[index_remove], self.rand_list[-1] = self.rand_list[-1], self.rand_list[index_remove]
        # remove
        self.rand_list.pop()
        self.rand_val_dict.pop(val)
        return True

    def getRandom(self) -> int:
        # print(self.rand_val_dict, self.rand_index_dict, self.size)
        index = random.randint(0, len(self.rand_list) - 1)  # [a,b] close interval
        return self.rand_list[index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()