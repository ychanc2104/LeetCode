# https://leetcode.com/problems/partition-array-for-maximum-sum/description/
# https://leetcode.com/problems/partition-array-for-maximum-sum/solutions/290863/java-c-python-dp-o-k-space/


# bottom-up dp, TC:O(NM), SC:O(N)
def maxSumAfterPartitioning(arr: List[int], k: int) -> int:
    # dp[i]: max sum of arr[:i+1]
    n = len(arr)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        value = 0
        for j in range(1, min(i, k) + 1):
            value = max(value, arr[i - j])
            dp[i] = max(dp[i], value * j + dp[i - j])
    return dp[-1]


# bottom-up dp, TC:O(NM), SC:O(N)
def maxSumAfterPartitioning2(arr: List[int], k: int) -> int:
    # dp[i]: max sum of arr[:i]
    n = len(arr)
    dp = [0] * (n + 1)
    for i in range(1, n+1):
        value = arr[i-1]
        dp[i] = dp[i-1] + value
        for j in range(2, min(i, k)+1): # update max value
            value = max(value, arr[i-j])
            dp[i] = max(dp[i], value * j + dp[i-j])
    return dp[-1]