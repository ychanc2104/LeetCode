# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

import heapq

# first thought, TC:O(), SC:O()
def maxEvents(events: List[List[int]]) -> int:
    memo = {}

    def helper(i):
        if i in visited:
            return False
        visited.add(i)
        s, e = events[i]
        for d in range(s, e + 1):
            if d not in memo or helper(memo[d]):
                memo[d] = i
                return True
        return False

    for i in range(len(events)):
        visited = set()
        helper(i)
    return len(memo)


# use heap, TC:O(NlogN), SC:O(N)
def maxEvents2(events: List[List[int]]) -> int:
    events.sort(reverse=True)
    d = 0 # current day
    res = 0
    heap = [] # store end,
    while heap or events:
        if not heap: # jump to that day, reduce TC:O(d+NlogN) to O(NlogN)
            d = events[-1][0]
        # push all avaiable events into heap
        while events and d >= events[-1][0]:
            heapq.heappush(heap, (events.pop()[1]))
        if heap:
            heapq.heappop(heap) # select one to attand
            res += 1
        d += 1
        # remove close event
        while heap and d > heap[0]:
            heapq.heappop(heap)
    return res