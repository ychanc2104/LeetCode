# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# first thought, modify node val, TC:O(n), SC:O(1)
def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head.next:
        return None
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid_next = slow.next
    if not mid_next:
        head.next = None
        return head
    slow.val = mid_next.val
    slow.next = mid_next.next
    return head

# TC:O(n), SC:O(1)
def deleteMiddle2(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head.next:
        return None
    slow = head
    fast = head.next.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    slow.next = slow.next.next
    return head