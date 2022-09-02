# https://leetcode.com/problems/find-median-from-data-stream/
# https://leetcode.com/problems/find-median-from-data-stream/discuss/74062/Short-simple-JavaC%2B%2BPython-O(log-n)-%2B-O(1)
# follow-up, https://leetcode.com/problems/find-median-from-data-stream/discuss/275207/Solutions-to-follow-ups
"""

1. If all integer numbers from the stream are between 0 and 100, how would you optimize it?

We can maintain an integer array of length 100 to store the count of each number along with a total count. Then, we can iterate over the array to find the middle value to get our median.

Time and space complexity would be O(100) = O(1).

2. If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

(In this case, we need an integer array of length 100 and a hashmap for these numbers that are not in [0,100].)

I dont' think we need hashmap.
As 99% is between 0-100. So can keep a counter for less_than_hundred and greater_than_hundred.
As we know soluiton will be definately in 0-100 we don't need to know those number which are >100 or <0, only count of them will be enough.


"""



import heapq


class MedianFinder:

    def __init__(self):
        self.small = [] # to get max
        self.large = [] # to get min
    # TC: O(logn)
    def addNum(self, num: int) -> None:
        # add to small
        heapq.heappush(self.small, -num)
        # check all small <= large
        if len(self.small)>0 and len(self.large)>0 and -self.small[0] > self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        # check length
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        ns = len(self.small)
        nl = len(self.large)
        #print(self.small, self.large)
        if (ns+nl)%2==1:
            return self.large[0] if nl>ns else -self.small[0]
        else:
            return (-self.small[0] + self.large[0])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


class MedianFinder2:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # initially add to small
        heapq.heappush(self.small, -num)
        # pop small to large heap
        heapq.heappush(self.large, -heapq.heappop(self.small))
        # pop large to small if length of large is bigger
        # maintain length of large <= small
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            # odd number
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0])/2


class MedianFinder3:

    def __init__(self):
        # min heap
        self.small = [] # negative, pop out the largest
        self.large = [] # pop out the smallest

    # TC:O(logN) for one operation, amortized TC:O(logN!/N)
    def addNum(self, num: int) -> None:
        heapq.heappush(self.large, num)
        # push min in large to the small. small size is bigger
        heapq.heappush(self.small, -heapq.heappop(self.large))
        if len(self.small) > len(self.large):
            # now large is bigger
            heapq.heappush(self.large, -heapq.heappop(self.small))

    # TC:O(1)
    def findMedian(self) -> float:
        # if size of small and large is equal => take average
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0])/2
        return self.large[0]