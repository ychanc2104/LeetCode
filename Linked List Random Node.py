# https://leetcode.com/problems/linked-list-random-node/description/

import random


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.memo = {}
        i = 0
        while head:
            self.memo[i] = head.val
            i += 1
            head = head.next
        self.size = i

    def getRandom(self) -> int:
        idx = random.randint(0, self.size - 1)
        return self.memo[idx]


# Reservoir sampling
class Solution2:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        head = self.head
        weight = 1
        res = head.val
        while head:
            if random.random() < 1 / weight:
                res = head.val
            head = head.next
            weight += 1
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()