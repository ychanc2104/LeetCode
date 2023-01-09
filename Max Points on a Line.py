# https://leetcode.com/problems/max-points-on-a-line/

import collections

# count slope, TC:O(N^2), SC:O(N^2)
def maxPoints(points: List[List[int]]) -> int:
    # hash map to count slope
    slope = lambda p1, p2: (p2[1] - p1[1]) / (p2[0] - p1[0]) if p2[0] - p1[0] != 0 else float('inf')
    counter = collections.Counter()  # start, slope
    n = len(points)
    res = 1
    for i in range(n):
        x1, y1 = points[i]
        for j in range(n):
            if i == j: continue
            s = slope(points[i], points[j])
            counter[(x1, y1, s)] += 1
            res = max(res, counter[(x1, y1, s)] + 1)
    return res


# count slope, TC:O(N^2), SC:O(N)
def maxPoints2(points: List[List[int]]) -> int:
    # hash map to count slope
    slope = lambda p1,p2: (p2[1]-p1[1])/(p2[0]-p1[0]) if p2[0]-p1[0]!=0 else float('inf')
    n = len(points)
    res = 1
    for i in range(n):
        counter = collections.Counter() # slope
        for j in range(n):
            if i == j: continue
            s = slope(points[i], points[j])
            counter[s] += 1
            res = max(res, counter[s] + 1)
    return res