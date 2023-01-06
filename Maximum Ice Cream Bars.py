# https://leetcode.com/problems/maximum-ice-cream-bars/description/

# first thought, sort, TC:O(NlogN), SC:O(N)
def maxIceCream(costs: List[int], coins: int) -> int:
    costs.sort()
    count = 0
    for c in costs:
        if coins - c < 0:
            break
        coins -= c
        count += 1
    return count

# bucket sort, TC:O(N+M), SC:O(N)
def maxIceCream2(costs: List[int], coins: int) -> int:
    bucket = {}
    M = 0
    for c in costs:
        bucket[c] = bucket.get(c, 0) + 1
        M = max(M, c)
    count = 0
    for cost in range(1, M + 1):
        freq = bucket.get(cost, 0)
        count += min(freq, coins // cost)
        coins -= cost * freq
        if coins < 0:
            break
    return count