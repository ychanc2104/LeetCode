# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# first thought, TC:O(NlogN), SC:O(logN)
def sortedListToBST(head: Optional[ListNode]) -> Optional[TreeNode]:
    def getMid(head):
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid

    def helper(head):
        if not head:
            return None
        if not head.next: # one node remaining
            return TreeNode(head.val)
        mid = getMid(head) # O(N/2+2*N/4+4*N/8+...) = O(N/2*logN)
        root = TreeNode(mid.val)
        root.left = helper(head)
        root.right = helper(mid.next)
        return root

    return helper(head)

# convert to array first, getMid => O(1), TC:O(N), SC:O(N)
def sortedListToBST2(head: Optional[ListNode]) -> Optional[TreeNode]:
    # TC:O(N)
    arr = []
    while head:
        arr.append(head.val)
        head = head.next

    def helper(L, R):
        if L > R:
            return None
        if L == R:  # one node
            return TreeNode(arr[L])
        mid = (L + R) // 2
        root = TreeNode(arr[mid])
        root.left = helper(L, mid - 1)
        root.right = helper(mid + 1, R)
        return root

    return helper(0, len(arr) - 1)