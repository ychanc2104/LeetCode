# https://leetcode.com/problems/merge-k-sorted-lists/


import heapq

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




list1 = build_ListNode([1,2,4])
list2 = build_ListNode([1,3,4,7,8])
list3 = build_ListNode([2,6])

lists = [list1, list2, list3]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## compare one by one using heapq, t: O(N*log(k)) and sapce: O(n+k)
def mergeKLists1(lists):
    ListNode.__lt__ = lambda self, other : self.val<other.val
    import heapq
    heap = []
    for l in lists:
        if l:
            heapq.heappush(heap, l)
    ans = ListNode()
    dummy = ans
    ## t, O(N), total N nodes
    while heap:
        ## t, O(logk), k lists here
        node = heapq.heappop(heap)
        dummy.next = node
        dummy = dummy.next
        node = node.next
        if node:
            heapq.heappush(heap, node)
    return ans.next


# TC:O(mn), m is size of lists, n is max size of linked list, SC:O(k)
def mergeKLists2(lists):
    k = len(lists)
    stored_lists = [head.val if head else float("inf") for head in lists]
    res = dummy = ListNode(-1)
    # O(m*k) in total
    while stored_lists != [float("inf")] * k:
        # O(k)
        m = min(stored_lists)
        # O(k)
        i_m = stored_lists.index(m)
        dummy.next = ListNode(m)
        dummy = dummy.next
        lists[i_m] = lists[i_m].next
        stored_lists[i_m] = lists[i_m].val if lists[i_m] else float("inf")
    return res.next


# use priority queue, t: O(N*log(k)) and sapce: O(n+k)
def mergeKLists3(lists):
    stored_lists = [(head.val, i) if head else (float("inf"), i) for i, head in enumerate(lists)]
    heapq.heapify(stored_lists)
    res = dummy = ListNode(-1)
    # O(n*logk) in total
    while stored_lists and stored_lists[0][0] != float("inf"):
        val, index = heapq.heappop(stored_lists)
        # O(logk)
        dummy.next = ListNode(val)
        dummy = dummy.next
        lists[index] = lists[index].next
        if lists[index]:
            heapq.heappush(stored_lists, (lists[index].val, index))
        else:
            heapq.heappush(stored_lists, (float("inf"), index))
    return res.next



a = [[],[]]
b = [x for list in a for x in list]








