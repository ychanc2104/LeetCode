# https://leetcode.com/problems/reverse-linked-list/
# https://leetcode.com/problems/reverse-linked-list/discuss/803955/C%2B%2B-Iterative-vs.-Recursive-Solutions-Compared-and-Explained-~99-Time-~85-Space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        head_r = temp = ListNode()
        while stack:
            v = stack.pop()
            temp.next = ListNode(v)
            temp = temp.next
        return head_r.next

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:

        pre = None
        while head:
            # store head.next
            temp = head.next
            # in-place assign to pre
            head.next = pre
            # store temp result(head) as pre
            pre = head
            # restore head to initially head.next
            head = temp

        return pre


    def reverseList3(self, head):
        res = None
        while head:
            temp = head.next
            head.next = res
            res = head
            head = temp
        return res