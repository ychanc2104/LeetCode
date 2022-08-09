# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# three pointers, TC:O(N), SC:O(1)
def oddEvenList(head):
    if not head:
        return head
    dummy = head
    odd = head
    even = head.next
    evenHead = head.next
    while even and even.next:
        # connect two odd nodes
        odd.next = even.next
        head = even.next
        # move all even nodes to evenHead
        even.next = head.next
        # initialize odd and even nodes
        odd = head
        even = head.next

    head.next = evenHead
    return dummy

# two pointers, TC:O(N), SC:O(1)
def oddEvenList2(head):
    if not head:
        return head
    dummy = head
    odd = head
    even = odd.next
    evenHead = even
    while even and even.next:
        # connect two odd nodes
        odd.next = even.next
        # initialize odd
        odd = odd.next
        # move all even nodes to evenHead
        even.next = odd.next
        # jump to next even node
        even = even.next

    odd.next = evenHead
    return dummy