# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/8802/3-short-Python-solutions


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# two-pass, TC:O(N), SC:O(1)
def removeNthFromEnd(head, n: int):
    # touch the end => get nth, n+1 th node => remove nth node
    count = 0
    temp = head
    while temp:
        temp = temp.next
        count += 1
    pos = count - n - 1
    if pos < 0:
        return head.next
    node = head
    for i in range(pos):
        node = node.next
    node.next = node.next.next
    return head

# two-pass, two pointers TC:O(N), SC:O(1)
def removeNthFromEnd2(head, n: int):
    # two pointers, separate n node between two pointers
    first = second = head
    for _ in range(n):
        first = first.next
    if not first:
        return second.next
    while head.next:
        second = second.next
        first = first.next
    second.next = second.next.next
    return head

# recursively
def removeNthFromEnd3(head, n: int):
    def remove(node):
        if not node:
            return 0, node
        # build head from the end
        i, node.next = remove(node.next)
        if i + 1 == n:
            # next node is to be removed
            return i + 1, node.next
        else:
            return i + 1, node

    i, head = remove(head)
    return head