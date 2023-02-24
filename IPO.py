# https://leetcode.com/problems/ipo/description/
# https://leetcode.com/problems/ipo/solutions/98216/python-priority-queue-with-explanation/


import heapq

# greedy + heaps, TC:O(nlogn), SC:O(n)
def findMaximizedCapital(k: int, w: int, profits: List[int], capital: List[int]) -> int:
    n = len(profits)
    info = sorted(zip(capital, profits))
    heaps = []
    p = 0
    for i in range(k):
        # push candidates into heaps
        while p < n and info[p][0] <= w:
            heapq.heappush(heaps, -info[p][1])
            p += 1
        if not heaps:
            break
        w += -heapq.heappop(heaps)  # valid max profit until now
    return w