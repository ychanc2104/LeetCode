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


# iterative method, TC:O(N), SC:O(1)
def reverseKGroup2(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy = head
    ktail = None
    res = None
    while dummy:
        count = 0
        while dummy and count < k:
            dummy = dummy.next
            count += 1
        # 1->2->3
        if count != k:
            break
        dummy2 = head
        R = None
        for i in range(k):
            dummy2_next = dummy2.next
            dummy2.next = R
            R = dummy2
            dummy2 = dummy2_next
        if not res: # store res
            res = R
        if ktail: # connect
            ktail.next = R
        ktail = head
        head = dummy
    if head:
        ktail.next = head
    return res if res else head # no need to reverse => return head