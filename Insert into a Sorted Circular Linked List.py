# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/description/


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

# first thought, TC:O(N), SC:O(1)
def insert(head: 'Optional[Node]', insertVal: int) -> 'Node':
    if not head:
        head = Node(insertVal)
        head.next = head
        return head
    # if min insert or max insert
    dummy = max_node = head
    while dummy != head.next and not head.val <= insertVal <= head.next.val:
        head = head.next
        if head.val >= max_node.val:
            max_node = head
    if insertVal < max_node.next.val or insertVal > max_node.val:  # min or max cases
        head = max_node
    head.next = Node(insertVal, head.next)
    return dummy


# clean, TC:O(N), SC:O(1)
def insert2(head: 'Optional[Node]', insertVal: int) -> 'Node':
    if not head:
        head = Node(insertVal)
        head.next = head
        return head
    # if min insert or max insert
    dummy = max_node = head
    while dummy != head.next:
        if head.val <= insertVal <= head.next.val: # inserted pos
            break
        if head.val > head.next.val and (insertVal > head.val or insertVal < head.next.val):
            break # min or max cases
        head = head.next
    head.next = Node(insertVal, head.next)
    return dummy