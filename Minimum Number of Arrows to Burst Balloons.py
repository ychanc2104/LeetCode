# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/


# first thought, TC:O(NlogN), SC:O(N)
def findMinArrowShots(points: List[List[int]]) -> int:
    points.sort()
    res = len(points)
    s, e = points[0]
    for i in range(1, len(points)):
        s2, e2 = points[i]
        if s2 <= e:  # overlapping with previous balloon
            e = min(e, e2)
            res -= 1
        else:
            e = e2  # new balloon
    return res


def findMinArrowShots2(points: List[List[int]]) -> int:
    if len(points) == 0:
        return 0
    points = sorted(points, key= lambda x:x[1])
    count = 1
    cur_max = points[0][1]
    for i in range(1, len(points)):
        if points[i][0] > cur_max:
            count += 1
            cur_max = points[i][1]
    return count