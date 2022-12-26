# https://leetcode.com/problems/design-circular-queue/


# two pointers
class MyCircularQueue:

    # TC:O(k), SC:O(k) for construction
    def __init__(self, k: int):
        self.queue = [-1] * k
        self.k = k
        self.front = 0
        self.rear = -1
        self.size = 0

    # TC:O(1)
    def enQueue(self, value: int) -> bool:
        if self.size >= self.k:
            return False
        self.rear += 1
        self.queue[self.rear % self.k] = value
        self.size += 1
        return True

    # TC:O(1)
    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.front += 1
        self.size -= 1
        return True

    # TC:O(1)
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front % self.k]

    # TC:O(1)
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear % self.k]

    # TC:O(1)
    def isEmpty(self) -> bool:
        return self.size == 0

    # TC:O(1)
    def isFull(self) -> bool:
        return self.size == self.k

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()