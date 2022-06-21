class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __iter__(self):
        temp = self
        while temp:
            yield temp.val
            temp = temp.next
    def __repr__(self):
        return ','.join([str(s) for s in self])


def build_ListNode(list):
    list_node = ListNode()
    temp = list_node
    for l in list:
        node = ListNode(l)
        temp.next = node
        temp = node
    return list_node.next

def mergeTwoLists(list1, list2):
    merged_list = temp = ListNode() ## same memory address
    while list1 and list2:
        if list1.val<list2.val:
            temp.next = list1 ## also assign merged_list.next
            list1 = list1.next ## switch to next list
        else:
            temp.next = list2
            list2 = list2.next
        temp = temp.next ## switch to merged_list.next
    temp.next = list1 if list1 else list2 ## append remainings
    return merged_list.next

# recursive method
def mergeTwoLists2(list1, list2):
    # escape for remaining list1 or list2
    if not (list1 and list2):
        return list1 or list2
    # top-down
    if list1.val <= list2.val:
        # list1.next assign to remaining list1 or list2
        list1.next = mergeTwoLists2(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists2(list1, list2.next)
        return list2



list1 = build_ListNode([1,2,4])
list2 = build_ListNode([1,3,4,7,8])

merged_list = mergeTwoLists(list1, list2)


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next


