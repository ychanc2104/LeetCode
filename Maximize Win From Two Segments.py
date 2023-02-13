# https://leetcode.com/problems/maximize-win-from-two-segments/description/
# https://leetcode.com/problems/maximize-win-from-two-segments/solutions/3141449/java-c-python-dp-sliding-segment-o-n/
# https://leetcode.com/problems/maximize-win-from-two-segments/solutions/3154943/easy-sliding-window-with-dp-visual-example/?orderBy=most_votes


# dp + sliding window, TC:O(N), SC:O(N)
def maximizeWin(prizePositions: List[int], k: int) -> int:
    # dp[i]: max for one segment, from 0 idx to i(exclusive)
    n = len(prizePositions)
    dp = [0] * (n + 1)
    L = 0
    res = 0
    for R in range(n):
        while prizePositions[L] + k < prizePositions[R]:
            L += 1  # invalid => contract window
        dp[R + 1] = max(dp[R], R - L + 1)  # update max number
        res = max(res, R - L + 1 + dp[L])  # current window, [L,R] + max in [0,L]
    return res