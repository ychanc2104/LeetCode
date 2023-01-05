# https://leetcode.com/problems/design-linked-list/


class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.head.prev = Node(val, next=self.head)
            self.head = self.head.prev
        self.n += 1

    def addAtTail(self, val: int) -> None:
        if not self.tail:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val, prev=self.tail)
            self.tail = self.tail.next
        self.n += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.n:
            self.addAtTail(val)
        elif index > self.n:
            return
        else:
            node = self.get_node(index)
            node_prev = node.prev
            new_node = Node(val, next=node, prev=node_prev)
            node_prev.next = new_node
            node.prev = new_node
            self.n += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.n:
            return
        node = self.get_node(index)
        node_prev = node.prev
        node_next = node.next
        if node_prev:
            node_prev.next = node_next
        else:  # at head
            self.head = node_next
        if node_next:
            node_next.prev = node_prev
        else:  # at tail
            self.tail = node_prev
        self.n -= 1

    def get_node(self, index):
        if index < 0 or index > self.n:
            return None
        head = self.head
        for i in range(index):
            head = head.next
        return head

    def get(self, index):
        node = self.get_node(index)
        return node.val if node else -1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)