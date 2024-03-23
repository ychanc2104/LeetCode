# https://leetcode.com/problems/reorder-list/description/?envType=daily-question&envId=2024-03-23

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# TC:O(N), SC:O(N)
def reorderList(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    deque = collections.deque([])

    dummy = head
    while dummy.next:
        dummy = dummy.next
        deque.append(dummy)

    rev = False
    while deque:
        head.next = deque.popleft() if rev else deque.pop()
        rev = not rev
        head = head.next
    head.next = None

# TC:O(N), SC:O(1)
def reorderList2(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """

    def reverse(head):
        res = None
        while head:
            head_next = head.next
            head.next = res
            res = head
            head = head_next
        return res

    if not head.next: return

    slow = fast = head
    fast = fast.next.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # merge two list
    slow_next = slow.next
    slow.next = None
    mid_rev = reverse(slow_next)
    while mid_rev:
        head_next = head.next
        head.next = mid_rev
        head = head.next
        mid_rev = head_next