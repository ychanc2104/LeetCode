# https://leetcode.com/problems/new-21-game/description/
# https://leetcode.com/problems/new-21-game/solutions/3560518/image-explanation-complete-intuition-maths-probability-dp-sliding-window-c-java-python/

# dp, TC:O(N^2), SC:O(N)
def new21Game(n: int, k: int, maxPts: int) -> float:
    # >k
    # dp[i], prob. to get i points
    # dp[i] = sum(dp[i-j-1] for j in range(maxPts))
    dp = [1] + [0] * n  # max is k+maxPts-1
    # print(dp)
    for i in range(1, n + 1):
        for j in range(1, maxPts + 1):
            if i - j >= 0 and i - j < k:
                dp[i] += dp[i - j] / maxPts

    # print(dp)
    return sum(dp[k:])

# dp + sliding window, TC:O(N), SC:O(N)
def new21Game2(n: int, k: int, maxPts: int) -> float:
    # >k
    # dp[i], prob. to get i points
    # dp[i] = sum(dp[i-j-1] for j in range(maxPts))
    if k == 0:
        return 1
    if n >= k + maxPts:
        return 1
    dp = [1] + [0] * n  # max is k+maxPts-1
    windowSum = 1
    # print(dp)
    for i in range(1, n + 1):
        dp[i] = windowSum / maxPts

        if i < k:
            windowSum += dp[i]

        if i >= maxPts:
            windowSum -= dp[i - maxPts]

    return sum(dp[k:])


# dp + sliding window, TC:O(N), SC:O(N)
def new21Game3(n: int, k: int, maxPts: int) -> float:
    # >k
    # dp[i], prob. to get i points
    # dp[i] = sum(dp[i-j-1] for j in range(maxPts))
    ans = [0]*k + [1]*(n-k+1) + [0]*maxPts
    val = sum(ans[k:k+maxPts])
    for i in reversed(range(k)):
        ans[i] = val/maxPts
        val += ans[i] - ans[i+maxPts]
    return ans[0]