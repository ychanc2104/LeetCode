# https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/


import collections


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# first thought, dfs, TC:O(N), SC:O(N)
def deleteDuplicatesUnsorted(head: ListNode) -> ListNode:
    counter = collections.Counter()
    dummy = ListNode(0, head)
    while head:
        counter[head.val] += 1
        head = head.next
    def dfs(head):
        if not head:
            return None
        head.next = dfs(head.next)
        if counter[head.val] == 1:
            return head
        return head.next
    dfs(dummy)
    return dummy.next


# iterative, TC:O(N), SC:O(N)
def deleteDuplicatesUnsorted2(head: ListNode) -> ListNode:
    counter = collections.Counter()
    dummy = head
    while head:
        counter[head.val] += 1
        head = head.next
    head = dummy
    prev = res = ListNode(0)
    while head:
        if counter[head.val] == 1: # preserve
            prev.next = head
            prev = prev.next
        head = head.next
    prev.next = None
    return res.next