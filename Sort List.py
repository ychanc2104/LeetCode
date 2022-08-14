# https://leetcode.com/problems/sort-list/
# https://leetcode.com/problems/sort-list/discuss/892759/Python-O(n-log-n-log-n)-merge-sort-explained

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# recursive merged sort, TC:O(nlogn), SC:O(logn) for recursive calls
def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    # divide and conguer
    mid = findMid(head)
    L = sortList(head)
    R = sortList(mid)
    # merge
    dummy = merged = ListNode(-1)
    while L and R:
        if L.val < R.val:
            # append L
            dummy.next = L
            dummy = dummy.next
            L = L.next
        else:
            # append R
            dummy.next = R
            dummy = dummy.next
            R = R.next
    if L:
        dummy.next = L
    else:
        dummy.next = R
    return merged.next

def findMid(head):
    # 1->2->3->4->5
    slow = head
    fast = head
    # exit loop earlier
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    # divide head into two linked lists
    mid = slow.next
    slow.next = None
    return mid

# iterative sort, TC:O(nlogn), SC:O(1) for recursive calls
def sortList2(head: Optional[ListNode]) -> Optional[ListNode]:
    def getsize(head):
        c = 0
        while head:
            head = head.next
            c += 1
        return c


    def split(head, size):
        tail = head
        for _ in range(size - 1):
            if not tail:
                return None
            tail = tail.next

        if not tail: return None
        next_head, tail.next = tail.next, None

        return next_head


    def merge(l1, l2, newtail):
        while l1 and l2:
            if l1.val <= l2.val:
                newtail.next = l1
                l1 = l1.next
            else:
                newtail.next = l2
                l2 = l2.next
            newtail = newtail.next

        newtail.next = l1 or l2
        while newtail.next:
            newtail = newtail.next

        return newtail


    length = getsize(head)
    newhead = ListNode(next=head)
    size = 1

    while size < length:
        newtail, cur = newhead, newhead.next
        while cur:
            h1 = cur
            h2 = split(h1, size)
            cur = split(h2, size)
            newtail = merge(h1, h2, newtail)
        size *= 2

    return newhead.next