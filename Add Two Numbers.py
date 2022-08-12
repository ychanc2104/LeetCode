# https://leetcode.com/problems/add-two-numbers/



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# TC:O(N+M), SC:O(max(N,M))
def addTwoNumbers(l1, l2):
    res = dummy = ListNode(-1)
    carry = 0
    while l1 or l2 or carry:
        if l1 and l2:
            if l1.val + l2.val + carry >= 10:
                res.next = ListNode(l1.val + l2.val - 10 + carry)
                carry = 1
            else:
                res.next = ListNode(l1.val + l2.val + carry)
                carry = 0
        elif l1:
            if l1.val + carry >= 10:
                res.next = ListNode(l1.val - 10 + carry)
                carry = 1
            else:
                res.next = ListNode(l1.val + carry)
                carry = 0
        elif l2:
            if l2.val + carry >= 10:
                res.next = ListNode(l2.val - 10 + carry)
                carry = 1
            else:
                res.next = ListNode(l2.val + carry)
                carry = 0
        else:
            res.next = ListNode(carry)
            carry = 0
        l1 = l1.next if l1 else l1
        l2 = l2.next if l2 else l2
        res = res.next
    return dummy.next

# TC:O(max(N,M)), SC:O(max(N,M))
def addTwoNumbers(l1, l2):
    res = dummy = ListNode(-1)
    carry = 0
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        if v1 + v2 + carry >= 10:
            res.next = ListNode(v1 + v2 - 10 + carry)
            carry = 1
        else:
            res.next = ListNode(v1 + v2 + carry)
            carry = 0
        l1 = l1.next if l1 else l1
        l2 = l2.next if l2 else l2
        res = res.next
    return dummy.next