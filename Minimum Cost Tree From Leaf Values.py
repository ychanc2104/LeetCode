# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/
# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/solutions/478708/rz-summary-of-all-the-solutions-i-have-learned-from-discuss-in-python/


import functools

# top-down dp, TC:O(N^3), SC:O(N^2)
def mctFromLeafValues(arr: List[int]) -> int:
    # dp[i][j]: ans of arr[i:j+1]
    n = len(arr)

    @functools.lru_cache(None)
    def helper(L, R):
        if L == R:
            return 0

        res = float('inf')
        for i in range(L, R):  # (0,0) + (1,2)
            res = min(res, helper(L, i) + helper(i + 1, R) + max(arr[L:i + 1]) * max(arr[i + 1:R + 1]))
        return res

    return helper(0, n - 1)


# bottom-up dp, TC:O(N^3), SC:O(N^2)
def mctFromLeafValues2(arr: List[int]) -> int:
    # dp[i][j]: ans of arr[i:j+1]
    n = len(arr)

    dp = [[float('inf')] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if i == j:
                dp[i][j] = 0  # initial value
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + max(arr[i:k + 1]) * max(arr[k + 1:j + 1]))

    return dp[0][-1]


# greedy, use min and its smaller neighbor first, TC:O(N^2), SC:O(1)
def mctFromLeafValues3(arr: List[int]) -> int:
    # dp[i][j]: ans of arr[i:j+1]
    res = 0
    while len(arr) > 1:
        idx = arr.index(min(arr))
        if 0 < idx < len(arr)-1:
            res += arr[idx] * min(arr[idx-1], arr[idx+1]) # use smaller neighbor first
        else: # directly use
            if idx == 0:
                res += arr[idx] * arr[idx+1]
            else: # end
                res += arr[idx] * arr[idx-1]
        arr.pop(idx) # delete min in arr
    return res

# use monotonic stack to compute smaller neighbor first, TC:O(N), SC:O(N)
def mctFromLeafValues4(arr: List[int]) -> int:
    # dp[i][j]: ans of arr[i:j+1]
    # 6,2,4,5  res = 8+20+30
    res = 0
    stack = []  # make stack monotonic decreasing, can exist equal num
    for node in arr:
        while stack and node > stack[-1]:
            nei = stack.pop()
            res += nei * min(node, stack[-1] if stack else float('inf'))
        stack.append(node)

    while len(stack) > 1:
        res += stack.pop() * stack[-1]

    return res