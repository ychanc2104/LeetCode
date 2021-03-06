# https://leetcode.com/problems/linked-list-cycle/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# first thought
def hasCycle(head) -> bool:
    if not head:
        return False
    slow = head
    faster = head.next
    while faster and faster.next and slow != faster:
        # print(slow.val, faster.val)
        faster = faster.next.next
        slow = slow.next
    if slow == faster:
        return True

    return False

# first thought, TC: O(N), SC: O(1)
def hasCycle2(head) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow==fast:
            return True
    return False