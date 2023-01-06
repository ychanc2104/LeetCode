# https://leetcode.com/problems/plus-one-linked-list/description/
# https://leetcode.com/problems/plus-one-linked-list/solutions/84130/java-recursive-solution/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# recursive, TC:O(N), SC:O(N)
def plusOne(head: ListNode) -> ListNode:
    dummy = head
    def dfs(head):
        if not head: return 1
        head.val += dfs(head.next)
        if head.val == 10:
            head.val = 0
            return 1
        return 0
    carry = dfs(dummy)
    if carry:
        return ListNode(1, head)
    return head


# iterative, TC:O(N), SC:O(1)
def plusOne2(head: ListNode) -> ListNode:
    # 1.find first non-nine node A from bottom, A.val += 1
    # 2.all nodes after A to be value=0
    dummy = ListNode(0, head)
    non_nine = dummy
    while head:
        if head.val != 9:
            non_nine = head
        head = head.next
    non_nine.val += 1
    # make all nodes after non_nine to be 0
    while non_nine.next:
        non_nine.next.val = 0
        non_nine = non_nine.next
    return dummy if dummy.val else dummy.next