# https://leetcode.com/problems/uncrossed-lines/description/
# https://leetcode.com/problems/uncrossed-lines/solutions/282842/java-c-python-dp-the-longest-common-subsequence/


import functools

# first thought, top-down dp, TC:O(NM), SC:O(NM)
def maxUncrossedLines(nums1: List[int], nums2: List[int]) -> int:
    @functools.lru_cache(None)
    def helper(p1, p2):
        if p1 == len(nums1) or p2 == len(nums2):
            return 0
        conn1 = 0
        if nums1[p1] == nums2[p2]:
            conn1 = 1 + helper(p1 + 1, p2 + 1)

        conn2 = max(helper(p1, p2 + 1), helper(p1 + 1, p2))
        return max(conn1, conn2)

    return helper(0, 0)

# bottom-up 2d dp, TC:O(NM), SC:O(NM)
def maxUncrossedLines2(nums1: List[int], nums2: List[int]) -> int:
    n, m = len(nums1), len(nums2)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if nums1[i-1] == nums2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1] # from last not matched position
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]


# bottom-up 1d dp, TC:O(NM), SC:O(NM)
def maxUncrossedLines3(nums1: List[int], nums2: List[int]) -> int:
    n, m = len(nums1), len(nums2)
    dp = [0] * (m+1)
    for i in range(1, n+1):
        dp_prev = dp.copy()
        for j in range(1, m+1):
            if nums1[i-1] == nums2[j-1]:
                dp[j] = 1 + dp_prev[j-1] # from last not matched position
            else:
                dp[j] = max(dp_prev[j], dp[j-1])
    return dp[-1]