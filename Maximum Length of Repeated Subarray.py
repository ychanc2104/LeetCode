# https://leetcode.com/problems/maximum-length-of-repeated-subarray/

# dp, TC:O(MN), SC:O(MN)
def findLength(nums1: List[int], nums2: List[int]) -> int:
    # dp[i][j] be the length of the longest common subarray starting at A[i] and B[j].
    n, m = len(nums1), len(nums2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if nums1[i] == nums2[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
    return max(max(row) for row in dp)