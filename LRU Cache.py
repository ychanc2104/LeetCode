# https://leetcode.com/problems/lru-cache/
# https://leetcode.com/problems/lru-cache/discuss/45952/Python-concise-solution-with-comments-(Using-OrderedDict).
# https://leetcode.com/problems/lru-cache/discuss/352295/Python3-doubly-linked-list-and-dictionary

import collections

## using doubly linked lists
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.dic = dict()  # key to node
        self.capacity = capacity
        self.head = ListNode(0, 0)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:  # similar to get()
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            node.value = value  # replace the value len(dic)
        else:
            if len(self.dic) >= self.capacity:
                self.removeFromTail()
            node = ListNode(key, value)
            self.dic[key] = node
            self.insertIntoHead(node)

    def removeFromList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insertIntoHead(self, node):
        headNext = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = headNext
        headNext.prev = node

    def removeFromTail(self):
        if len(self.dic) == 0: return
        tail_node = self.tail.prev
        del self.dic[tail_node.key]
        self.removeFromList(tail_node)


# using OrderedDict
class LRUCache2:
    def __init__(self, capacity):
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)
        self.dic[key] = v   # set key as the newest one
        return v

    def set(self, key, value):
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:  # self.dic is full
                self.dic.popitem(last=False)
        self.dic[key] = value


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache3:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head = Node(0, 0)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    # TC: O(1)
    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        # get key and add to the head
        node = self.dict[key]
        # delete node
        node_next = node.next
        node_prev = node.prev
        node_next.prev = node_prev
        node_prev.next = node_next
        # add to head
        head_next = self.head.next
        self.head.next = node
        head_next.prev = node
        node.prev = self.head
        node.next = head_next

        return node.value

    # TC: O(1)
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            # update value, do something same with get
            node = self.dict[key]
            node.value = value
            self.get(key)
        else:
            # check len(self.dict)
            if len(self.dict) == self.capacity:
                # get and remove tail
                tail = self.tail.prev
                tail_prev = tail.prev
                self.tail.prev = tail_prev
                tail_prev.next = self.tail
                del self.dict[tail.key]
            # add new node to the head
            node = Node(key, value)
            self.dict[key] = node
            head_next = self.head.next
            self.head.next = node
            node.prev = self.head
            node.next = head_next
            head_next.prev = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

cache = LRUCache(4)
cache.put(1,1)
cache.put(2,2)
cache.get(1)