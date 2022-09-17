# https://leetcode.com/problems/kth-largest-element-in-a-stream/
# https://leetcode.com/problems/kth-largest-element-in-a-stream/discuss/148866/Python-simple-heapq-solution-beats-100
import heapq

# first thought
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [-n for n in nums]
        heapq.heapify(self.nums)
        self.large = []
        heapq.heapify(self.large)
        for i in range(k - 1):
            if not self.nums:
                break
            # leave k-1 elements in self.large
            large = heapq.heappop(self.nums)
            heapq.heappush(self.large, -large)

    def add(self, val: int) -> int:
        # push val into
        # -4,-2 and 5,8(large)
        if self.large and val >= self.large[0]:
            res = self.large[0]
            large = heapq.heappushpop(self.large, val)
            heapq.heappush(self.nums, -large)
            return res
        heapq.heappush(self.nums, -val)
        return -self.nums[0]



class KthLargest:
    # TC:O(nlogn), SC:O(k)
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        # leave k elements, top k largest
        for _ in range(len(nums) - k):
            heapq.heappop(self.nums)

    # TC:O(logk)
    def add(self, val: int) -> int:
        # 2,4,5,8 => 4,5,8
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)