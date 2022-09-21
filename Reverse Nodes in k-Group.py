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



# iterative method, TC:O(N), SC:O(1)
def reverseKGroup2(head: Optional[ListNode], k: int) -> Optional[ListNode]:
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

    dummy = head
    prev = None
    ktail = None
    while dummy:
        count = 0
        dummy = head
        while k > count and dummy:
            dummy = dummy.next
            count += 1
        # reverse k nodes
        if k == count:
            reverse = reversek(head, k)
            # store result
            if not prev:
                prev = reverse
            # connect original first node to second reverse node
            if ktail:
                ktail.next = reverse
            ktail = head
            head = dummy
    # still remain some nodes no need to reverse
    if ktail:
        ktail.next = head
    return prev if prev else head