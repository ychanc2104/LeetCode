# https://leetcode.com/problems/add-two-numbers-ii/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# first thought, reverse and add two number, TC:O(N+M), SC:O(1) output is not taking account
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def reverse(l):
        r = None
        while l:
            l_next = l.next
            l.next = r
            r = l
            l = l_next
        return r

    l1 = reverse(l1)
    l2 = reverse(l2)
    res = dummy = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
        carry = s // 10
        s %= 10
        dummy.next = ListNode(s)
        dummy = dummy.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return reverse(res.next)


# first thought, w/o reverse, TC:O(N+M), SC:O(1) output is not taking account
def addTwoNumbers2(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def getLength(l):
        node = l
        n = 0
        while node:
            n += 1
            node = node.next
        return n
    # 1.get length
    n1 = getLength(l1)
    n2 = getLength(l2)
    if n1 < n2:
        return addTwoNumbers2(l2, l1)
    # 2.n1 always >= n2, add two numbers
    dummy = None # reverse it
    while l1 or l2:
        s = 0
        if n1 > n2:
            s += (l1.val if l1 else 0)
            n1 -= 1
            l1 = l1.next if l1 else None
        elif n1 == n2:
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            n1 -= 1
            n2 -= 1
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        new_node = ListNode(s)
        new_node.next = dummy
        dummy = new_node
    print(dummy, dummy.val)

    # 3.deal with carry
    carry = 0
    res = None
    while dummy:
        s = dummy.val + carry
        new_node = ListNode(s%10)
        carry = s//10
        dummy = dummy.next
        new_node.next = res
        res = new_node
    print(carry)
    if carry:
        return ListNode(1, next=res)
    return res