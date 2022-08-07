# https://leetcode.com/problems/swap-nodes-in-pairs/
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# TC:O(n), SC:O(n) for recursive call
def swapPairs(head):
    # 1,2,3 => 2,1,3
    # recursive
    if not head or not head.next:
        # 1,2,3 => do nothing when head=3(stop swapping)
        return head

    firstNode = head
    secondNode = head.next

    ## swap
    firstNode.next = swapPairs(secondNode.next)
    secondNode.next = firstNode
    return secondNode

# iterative, TC:O(n), SC:O(1)
def swapPairs2(head):
    # 1,2,3 => 2,1,3
    dummy = ListNode(-1)
    dummy.next = head

    prev_node = dummy

    while head and head.next:
        firstNode = head
        secondNode = head.next
        # swap
        prev_node.next = secondNode
        firstNode.next = secondNode.next
        secondNode.next = firstNode

        prev_node = firstNode
        head = firstNode.next
    return dummy.next