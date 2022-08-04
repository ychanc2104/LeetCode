# https://leetcode.com/problems/longest-increasing-subsequence/
# https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326552/Optimization-From-Brute-Force-to-Dynamic-Programming-Explained!
# https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326308/C%2B%2BPython-DP-Binary-Search-BIT-Solutions-Picture-explain-O(NlogN)
#

# first thought

class Solution:
    def lengthOfLIS(self, nums) -> int:
        # brute force
        self.res = 0
        self.n = len(nums)

        def dfs(x, pos, ans):
            # print(x, pos, ans)
            if pos >= self.n:
                self.res = max(self.res, ans)
                return
            if x < nums[pos]:
                dfs(nums[pos], pos + 1, ans + 1)
                dfs(x, pos + 1, ans)
            else:
                dfs(x, pos + 1, ans)
        # O(2^N)
        for i in range(self.n):
            dfs(nums[i], i, 1)
        return self.res

## dp soln, TC: O(n^2), SC: O(n)
def lengthOfLIS2(nums) -> int:
    ## dp, bottom-up
    n = len(nums)
    dp = [1] * n # dp[i]: max length which starts from nums[i]
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            # j > i, iterately update dp[i], equivalently equal to dp[i] = max(1+dp[i+1], 1+dp[i+2],..., 1+dp[n-1])
            # compare with all dp, ex: dp[i+1], dp[i+2], ..., dp[n-1], and choose max
            if nums[i]<nums[j]:
                dp[i] = max(dp[i], 1+dp[j])
    return max(dp)


# TC: O(n^2) worst for all element is the same value and we should do linear scan everytime, SC:O(N)
def lengthOfLIS3(nums) -> int:
    sub = [nums[0]]
    for num in nums[1:]:
        # equal is to prevent [7,7,7,7] take into account
        if num<=sub[-1]:
            # find first element is greater than num and replace it
            i = 0
            # stop when sub[i]>=num
            while sub[i]<num:
                i += 1
            sub[i] = num
        else:
            sub.append(num)
    return len(sub)

# binary search, TC: O(nlogn), SC:O(N)
def lengthOfLIS4(nums) -> int:
    # to find the closet element in sub
    def binary_search(sub, target):
        L, R = 0, len(sub) - 1
        while L <= R:
            mid = L + (R - L) // 2
            if sub[mid] > target:
                # go left
                R = mid - 1
            elif sub[mid] < target:
                # go right
                L = mid + 1
            else:
                return mid
        return L
    sub = [nums[0]]
    for num in nums[1:]:
        i = binary_search(sub, num)
        # increaing case, directly append
        if i == len(sub):
            sub.append(num)
        else:
            sub[i] = num
    return len(sub)