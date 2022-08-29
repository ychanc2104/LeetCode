# https://leetcode.com/problems/rotate-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# first thought, TC:O(n), SC:O(1)
def rotateRight(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # TC:O(n)
    def get_size(head):
        size = 0
        while head:
            head = head.next
            size += 1
        return size
    # TC:O(n)
    size = get_size(head)
    if size <= 1 or k % size == 0 or not head:
        return head
    k = k % size
    dummy = head
    # TC: O(n-k)
    for _ in range(size - k - 1):
        dummy = dummy.next
    head_next = dummy.next
    dummy.next = None
    dummy_head_next = head_next
    while dummy_head_next.next:
        dummy_head_next = dummy_head_next.next
    dummy_head_next.next = head
    return head_next


# use cyclic linked lists and break the cycle, TC:O(n), SC:O(1)
def rotateRight2(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    # build cyclic linked lists
    dummy = head
    size = 1
    while dummy.next:
        dummy = dummy.next
        size += 1
    dummy.next = head
    # find position at size - k % size - 1
    dummy = head
    for _ in range(size - k%size - 1):
        dummy = dummy.next
    # save and break the cycle
    head_next = dummy.next
    dummy.next = None
    return head_next