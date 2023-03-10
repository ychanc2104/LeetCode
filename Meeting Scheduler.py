# https://leetcode.com/problems/meeting-scheduler/

import heapq


# two heaps, TC:O(NlogN + MlogM), SC:O(N+M)
def minAvailableDuration(slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
    heapq.heapify(slots1)
    heapq.heapify(slots2)

    while slots1 and slots2:
        # pop out smaller start
        s1, e1 = slots1[0]
        s2, e2 = slots2[0]
        d = min(e1, e2) - max(s1, s2)
        if d >= duration:
            return [max(s1, s2), max(s1, s2) + duration]
        if e1 > e2:
            heapq.heappop(slots2)
        else:
            heapq.heappop(slots1)

    return []



# scalable one heaps, TC:O((N+M)log(N+M)), SC:O(N+M)
def minAvailableDuration2(slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
    mix = slots1 + slots2
    heapq.heapify(mix)
    # heapq.heapify(slots2)
    start, end = heapq.heappop(mix)
    while mix:
        # pop out smaller start
        s1, e1 = heapq.heappop(mix)
        # s2, e2 = mix[0]
        d = min(e1, end) - max(s1, start)
        if d >= duration:
            return [max(s1, start), max(s1, start) + duration]
        if e1 > end: # update longer end
            start, end = s1, e1
    return []