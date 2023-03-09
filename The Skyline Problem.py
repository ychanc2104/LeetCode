# https://leetcode.com/problems/the-skyline-problem/
# https://leetcode.com/problems/the-skyline-problem/solutions/61261/11-line-python-solution-with-max-heap-easy-to-understand/

import heapq

# brute force, TC:O(N^2), SC:O(N)
def getSkyline(buildings: List[List[int]]) -> List[List[int]]:
    positions = sorted(set([x for l, r, h in buildings for x in (l, r)]))
    heights = [0] * len(positions)  # max height at position i
    idx = {x: i for i, x in enumerate(positions)}
    for l, r, h in buildings:
        il, ir = idx[l], idx[r]
        for j in range(il, ir):
            heights[j] = max(heights[j], h)

    res = []
    for i in range(len(heights)):
        if not res or res[-1][-1] != heights[i]:
            res.append([positions[i], heights[i]])

    return res

# brute force, TC:O(N^2), SC:O(N)
def getSkyline2(buildings: List[List[int]]) -> List[List[int]]:
    positions = sorted(set([x for l, r, h in buildings for x in (l, r)]))
    res = []
    for i in range(len(positions)):
        # update max height at positions[i]
        height = 0
        for l, r, h in buildings:
            if l <= positions[i] < r:
                height = max(height, h)
        if not res or res[-1][-1] != height:
            res.append([positions[i], height])

    return res

# use heap, TC:O(NlogN), SC:O(N)
def getSkyline3(buildings: List[List[int]]) -> List[List[int]]:
    events = []
    for L, R, H in buildings:
        # append start point of building
        events.append((L, -H, R))
        # append end point of building
        events.append((R, 0, 0))

    # sort the event
    events.sort()

    # init for result and heap
    res = []
    hp = [(0, float("inf"))]

    for pos, negH, R in events:
        # pop out building which is end
        while hp[0][1] <= pos:
            heapq.heappop(hp)

        # if it is a start of building, push it into heap as current building
        if negH != 0:
            heapq.heappush(hp, (negH, R))

        # if change in height with previous key point, append to result
        if not res or res[-1][1] != -hp[0][0]:
            res.append([pos, -hp[0][0]])

    return res