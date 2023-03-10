# https://leetcode.com/problems/linked-list-cycle-ii/description/
# https://leetcode.com/problems/linked-list-cycle-ii/solutions/1701128/c-java-python-slow-and-fast-image-explanation-beginner-friendly/?orderBy=most_votes

# two pointers, TC:O(N), SC:O(1)

def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return None
    slow = head.next
    fast = head.next.next
    while fast and fast.next and slow != fast:
        slow = slow.next
        fast = fast.next.next
    # a,x,C-x => 2*(a+x) = a+x+nC, a+x = nC => a=C-x
    while slow and head != slow:
        head = head.next
        slow = slow.next
    return slow if slow else None