# https://leetcode.com/problems/paint-house/description/


# dp + dfs, TC:O(3^N), SC:O(N)
def minCost(costs: List[List[int]]) -> int:
    @lru_cache(None)
    def dfs(house, prev=-1):
        # return current costs
        if house == len(costs):
            return 0

        cost = costs[house]
        res = float('inf')
        for i in range(3):
            if prev == i:
                continue
            res = min(res, cost[i] + dfs(house + 1, i))
        return res

    return dfs(0)


# bottom-up dp, TC:O(N), SC:O(1)
def minCost2(costs: List[List[int]]) -> int:
    f0 = f1 = f2 = 0
    for cost in costs:
        f0, f1, f2 = min(f1+cost[0], f2+cost[0]), min(f0+cost[1], f2+cost[1]), min(f0+cost[2], f1+cost[2]) # paint 0, 1, 2
    return min(f0, f1, f2)