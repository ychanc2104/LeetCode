# https://leetcode.com/problems/reverse-nodes-in-k-group/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# recursive method, TC:O(N), SC:O(N/k) for recursive depth
def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    def reversek(head, k):
        dummy = head
        reverse = None
        while k != 0:
            dummy_next = dummy.next
            dummy.next = reverse
            reverse = dummy
            dummy = dummy_next
            k -= 1
        return reverse

    count = 0
    dummy = head
    while k > count and dummy:
        dummy = dummy.next
        count += 1
        if k == count:
            reverse = reversek(head, k)
            head.next = reverseKGroup(dummy, k)  # connect to next reverse linked lists
            return reverse
    return head
