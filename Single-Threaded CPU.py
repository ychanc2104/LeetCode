# https://leetcode.com/problems/single-threaded-cpu/description/

import heapq

# use heaps, TC:O(NlogN), SC:O(N)
def getOrder(tasks: List[List[int]]) -> List[int]:
    heaps = [(et, pt, i) for i, (et, pt) in enumerate(tasks)]  #
    ava_tasks = []
    heapq.heapify(heaps)
    occupied_time = 0
    res = []
    while heaps or ava_tasks:
        
        while heaps and (heaps[0][0] <= occupied_time or not ava_tasks):
            et, pt, i = heapq.heappop(heaps)
            heapq.heappush(ava_tasks, (pt, i, et))
        # next task
        pt2, i2, et2 = heapq.heappop(ava_tasks)
        res.append(i2)
        occupied_time = max(et2, occupied_time) + pt2
    return res