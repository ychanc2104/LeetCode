# https://leetcode.com/problems/remove-stones-to-minimize-the-total/description/

import heapq

# first thought, use heaps, TC:O(klogN + N), SC:(N)
def minStoneSum(piles: List[int], k: int) -> int:
    heaps = [-p for p in piles]
    heapq.heapify(heaps)
    for _ in range(k):
        pile = heapq.heappop(heaps)
        pile *= -1
        heapq.heappush(heaps, -(pile - pile // 2))
    return -sum(heaps)