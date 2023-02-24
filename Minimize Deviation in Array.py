# https://leetcode.com/problems/minimize-deviation-in-array/description/
# https://leetcode.com/problems/minimize-deviation-in-array/solutions/952857/java-c-python-priority-queue/

import heapq


# TC:O(NlogN), SC:O(N)
def minimumDeviation(nums: List[int]) -> int:
    # odds can only double once
    heaps = []
    for num in nums:
        # smallest possible number and original number
        heapq.heappush(heaps, [num // (num & -num), num])

    res = float('inf')
    M = max(a for a, a0 in heaps)
    while len(heaps) == len(nums):
        a, a0 = heapq.heappop(heaps)
        res = min(res, M - a)
        if a % 2 or a < a0:  # we can get 2*a when a is odd or a < a0
            M = max(M, 2 * a)
            heapq.heappush(heaps, [2 * a, a0])
    return res