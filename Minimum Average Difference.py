# https://leetcode.com/problems/minimum-average-difference/description/
# https://leetcode.com/problems/minimum-average-difference/solutions/1994575/prefix-sum-o-1-space/

# first thought, prefix sum, TC:O(N), SC:O(N)
def minimumAverageDifference(nums: List[int]) -> int:
    # prefix sum
    prefix = []
    s = 0
    for num in nums:
        s += num
        prefix.append(s)
    n = len(nums)
    res = 0
    m = float("inf")
    for i in range(len(nums)):
        temp = abs(prefix[i] // (i + 1) - ((s - prefix[i]) // (n - 1 - i) if i != n - 1 else 0))
        if temp < m:
            res = i
            m = temp
    return res

# sapce optimized prefix sum, TC:O(N), SC:O(1)
def minimumAverageDifference2(nums: List[int]) -> int:
    s = 0
    for num in nums:
        s += num
    n = len(nums)
    res = 0
    m = float("inf")
    prefix = 0
    for i in range(len(nums)):
        prefix += nums[i]
        temp = abs(prefix//(i+1) - ((s - prefix)//(n-1-i) if i!=n-1 else 0))
        if temp < m:
            res = i
            m = temp
    return res