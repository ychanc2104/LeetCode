# https://leetcode.com/problems/paint-house-ii/


# first thought, bottom-up dp, TC:O(NM^2), SC:O(NM)
def minCostII(costs: List[List[int]]) -> int:
    n, m = len(costs), len(costs[0])
    dp = [[0] * m for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(m):
            dp[i][j] = float('inf')  # initialize
            for k in range(m):
                if j == k: continue
                dp[i][j] = min(dp[i][j], dp[i - 1][k] + costs[i - 1][j])
    return min(dp[-1])



# optimize time using first and second min, bottom-up dp, TC:O(NM), SC:O(NM)
def minCostII2(costs: List[List[int]]) -> int:
    def get_2min(nums):
        first, second = None, None
        for num in nums:
            if not first or num < first:
                second = first
                first = num
            elif not second or num < second:
                second = num
        return first, second

    n, m = len(costs), len(costs[0])
    dp = [[0] * m for _ in range(n + 1)]
    for i in range(1, n + 1):
        first, second = get_2min(dp[i - 1])
        for j in range(m):  # store first min and second min
            dp[i][j] = float('inf')  # initialize
            prev = first if dp[i - 1][j] != first else second
            dp[i][j] = min(dp[i][j], prev + costs[i - 1][j])

    return min(dp[-1])