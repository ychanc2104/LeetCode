# https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/description/


# Definition for polynomial singly-linked list.
class PolyNode:
    def __init__(self, x=0, y=0, next=None):
        self.coefficient = x
        self.power = y
        self.next = next

# merge two linked list, TC:O(min(N,M)), SC:O(1)
def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
    res = dummy = PolyNode()
    while poly1 and poly2:
        (c1, p1) = (poly1.coefficient, poly1.power)
        (c2, p2) = (poly2.coefficient, poly2.power)
        if p1 == p2:
            if c1 + c2 != 0:
                res.next = PolyNode(c1+c2, p1)
                res = res.next
            poly1 = poly1.next
            poly2 = poly2.next
        elif p1 > p2:
            res.next = PolyNode(c1, p1)
            res = res.next
            poly1 = poly1.next
        else:
            res.next = PolyNode(c2, p2)
            res = res.next
            poly2 = poly2.next
    res.next = poly1 if poly1 else poly2
    return dummy.next


x = PolyNode(1,1,PolyNode(2,0))