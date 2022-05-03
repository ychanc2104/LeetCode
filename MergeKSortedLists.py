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
class Solution:
    ## compare one by one, t: O(kN) and sapce: O(n+k)
    def mergeKLists(self, lists):
        ans = ListNode()
        dummy = ans
        compare_list = [l.val for l in lists if l]
        ## t, O(N), total N nodes
        while min(compare_list)!=float("inf") and compare_list:
            ## t, O(k), k lists here
            m = min(compare_list)
            i_m = compare_list.index(m)
            if lists[i_m]:
                lists[i_m] = lists[i_m].next
            compare_list[i_m] = lists[i_m].val if lists[i_m] else float("inf")
            dummy.next = ListNode(m)
            dummy = dummy.next
        return ans.next
    ## compare one by one using heapq, t: O(N*log(k)) and sapce: O(n+k)
    def mergeKLists2(self, lists):
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



a = [[],[]]
b = [x for list in a for x in list]








