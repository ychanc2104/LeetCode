# https://leetcode.com/problems/lfu-cache/description/
# https://leetcode.com/problems/lfu-cache/solutions/207673/python-concise-solution-detailed-explanation-two-dict-doubly-linked-list/




import collections

# TC:O(1) for each operation
class LFUCache:

    def __init__(self, capacity: int):
        self.memo = {}  # map key to node
        self.freq = collections.defaultdict(DLinkedList)  # store nodes of different freq
        self.min_freq = 1
        self.size = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.memo:
            return -1
        # add node counter and re-populate
        node = self.memo[key]
        self.update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:  # do nothing
            return
        if key in self.memo:
            self.memo[key].val = value  # update value
            self.update(self.memo[key])
        else:  # new node
            if self.size == self.capacity:  # reach limit, delete LFU first
                node_minf = self.freq[self.min_freq].pop()  # remove from dLL's head
                del self.memo[node_minf.key]  # totally delete
                self.size -= 1

            node = Node(value, key)
            self.memo[key] = node
            self.freq[1].append(node)
            self.min_freq = 1
            self.size += 1

    # update self.freq
    def update(self, node):
        f = node.freq
        self.freq[f].pop(node)  # remove from the tail this dLL
        if self.min_freq == f and not bool(self.freq[f]):  # matain min_freq
            self.min_freq += 1  # node is the last node in self.freq[f]
        node.freq += 1
        self.freq[node.freq].append(node)  # add node into new freq dLL
        return node


class Node:
    def __init__(self, val=None, key=None, freq=1, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev
        self.freq = freq


class DLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def __bool__(self):
        return self.size > 0

    def append(self, node):  # append node to the head
        head_next = self.head.next
        self.head.next = node
        node.next = head_next
        node.prev = self.head
        head_next.prev = node
        self.size += 1

    def pop(self, node=None):  # remove node from the tail and get node
        if not node:
            # remove from the tail(old one)
            node = self.tail.prev

        node_prev = node.prev
        node_next = node.next
        node_prev.next = node_next
        node_next.prev = node_prev
        self.size -= 1
        return node

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

