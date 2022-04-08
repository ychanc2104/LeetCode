class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

## build singlely linked list
def build_ListNode(list):
    list_node = ListNode()
    temp = list_node
    # list_node.next = temp
    for l in list:
        node = ListNode(l)
        temp.next = node
        temp = node
    return list_node.next

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, value):
        node = ListNode(value)
        if self.head==None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
    def delete(self): ## delete last
        current = self.head
        if current.next==None:
            self.head = None
            self.tail = None
        else:
            while current!=None:
                if current.next.next==None:
                    self.tail = current
                    self.tail.next = None
                    break
                current = current.next



l = SingleLinkedList()
l.append(10)
l.append(20)
# l.append(100)
l.delete()

a=[10]
b=a
a.append(20)
# a = ListNode(10)
# b = ListNode(20,a)