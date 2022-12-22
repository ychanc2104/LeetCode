# https://leetcode.com/problems/minimum-cost-to-connect-sticks/description/

import heapq

# first thought, heaps + greedy, TC:O(N + NlogN), SC:O(N)
def connectSticks(sticks: list[int]) -> int:
    heapq.heapify(sticks)
    res = 0
    while len(sticks) > 1:
        combine = heapq.heappop(sticks) + heapq.heappop(sticks)
        res += combine
        heapq.heappush(sticks, combine)
    return res