# https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/description/
# https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/solutions/3468268/dijkstra-s-algorithm-with-roads-as-edges/
# https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/solutions/3471042/no-dijkstra-just-bfs/

import heapq, collections


# Dijkstra, TC:O(), SC:O()
def minimumCost(start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
    # from i,j to end of roads or i,j to target

    specialRoads = [[x1, y1, x2, y2, c] for x1, y1, x2, y2, c in specialRoads if c < abs(x1 - x2) + abs(y1 - y2)]
    heaps = [(0, start[0], start[1])]
    dp = collections.defaultdict(lambda: float('inf'))
    dp[(start[0], start[1])] = 0  # from start to (i,j)
    while heaps:
        total, x, y = heapq.heappop(heaps)  # total: cost to (x,y)
        for x1, y1, x2, y2, c in specialRoads:
            cost_to_end = abs(x - x1) + abs(y - y1) + c
            # end_to_target = abs(x2 - target[0]) + abs(y2 - target[1])
            if dp[(x2, y2)] > total + cost_to_end:
                heapq.heappush(heaps, (total + cost_to_end, x2, y2))
                dp[(x2, y2)] = total + cost_to_end
    # print(dp)
    res = min(dp[(target[0], target[1])], abs(start[0] - target[0]) + abs(start[1] - target[1]))
    for x1, y1, x2, y2, c in specialRoads:
        res = min(res, dp[(x2, y2)] + abs(x2 - target[0]) + abs(y2 - target[1]))

    return res