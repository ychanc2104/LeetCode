# https://leetcode.com/problems/two-city-scheduling/


# greedy, TC:O(nlogn), SC:O(n)
def twoCitySchedCost(costs: List[List[int]]) -> int:
    costs.sort(key=lambda x: x[0] - x[1])
    n = len(costs)
    res = 0
    for i in range(n):
        if i < n // 2:
            res += costs[i][0]
        else:
            res += costs[i][1]
    return res