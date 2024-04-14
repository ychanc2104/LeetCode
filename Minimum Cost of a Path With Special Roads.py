# https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/description/
# https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/solutions/3468268/dijkstra-s-algorithm-with-roads-as-edges/
# https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/solutions/3471042/no-dijkstra-just-bfs/

import heapq, collections


# Dijkstra, TC:O(), SC:O()
def minimumCost(start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
    # dp(i,j): min cost from start to (i,j)
    def cal_dist(x1,y1,x2,y2):
        return abs(x1-x2) + abs(y1-y2)

    specialRoads = [road for road in specialRoads if road[-1] < cal_dist(*road[:-1])]
    dp = collections.defaultdict(lambda : float("inf"))
    heap = [(0, *start)]
    res = cal_dist(*start, *target)
    while heap:
        d, x, y = heapq.heappop(heap)
        res = min(res, dp[(x, y)] + cal_dist(x,y,*target))

        for x1,y1,x2,y2,cost in specialRoads:
            new_dist = d + cal_dist(x,y,x1,y1) + cost
            if dp[(x2, y2)] > new_dist:
                dp[(x2, y2)] = new_dist
                heapq.heappush(heap, (new_dist, x2, y2))

    return res