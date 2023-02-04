# https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/
# https://leetcode.com/problems/number-of-longest-increasing-subsequence/solutions/835323/python-3-dp-explanation/


def findNumberOfLIS(nums: List[int]) -> int:
    n = len(nums)
    dp = [1] * n
    cnt = [1] * n
    M = 1
    for i in range(n):  # 1, 2
        for j in range(i):  # 0, 0 1
            if nums[j] < nums[i]:
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1  # update longest length
                    cnt[i] = cnt[j]
                elif dp[i] == dp[j] + 1:  # new branch occurred
                    cnt[i] += cnt[j]
            M = max(M, dp[i])
    return sum(c for l, c in zip(dp, cnt) if l == M)