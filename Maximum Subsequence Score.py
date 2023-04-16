# https://leetcode.com/problems/maximum-subsequence-score/description/
# https://leetcode.com/problems/maximum-subsequence-score/description/


import heapq

# use heap, TC:O(NlogN), SC:O(N)
def maxScore(nums1: List[int], nums2: List[int], k: int) -> int:
    nums = sorted([(x, y) for x, y in zip(nums2, nums1)], reverse=True)
    n = len(nums)
    res = 0
    heap = []  # store top k-1 largest num
    curSum = 0  # sum of top k-1 largest num
    for i in range(n):
        heapq.heappush(heap, nums[i][1])
        curSum += nums[i][1]
        if i >= k - 1:
            res = max(res, nums[i][0] * curSum)
            curSum -= heapq.heappop(heap)
    return res