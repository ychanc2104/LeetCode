# https://leetcode.com/problems/palindrome-linked-list/
#

## first thought, use stack and find middle of linked lists, TC:O(n), SC:O(n)
def isPalindrome(head) -> bool:
    # 1. compare with reverse linked list
    # 2. stack? meet mid
    stack = []
    slow = head
    fast = head
    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
    # pop out and check from center
    # odd and even, decide from fast
    if fast:
        # odd
        slow = slow.next
    while slow:
        val = slow.val
        val_check = stack.pop()
        if val != val_check:
            return False
        slow = slow.next
    return True


# second thought, use find middle and reverse linked lists ,TC:O(n), SC:O(1)
def isPalindrome2(head) -> bool:
    # 1. compare with reverse linked list
    # 2. stack? meet mid
    # 3. reverse half portion
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    if fast:
        # odd, no need to deal with mid
        slow = slow.next
    # reverse slow
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
    while prev:
        if prev.val!=head.val:
            return False
        prev = prev.next
        head = head.next
    return True