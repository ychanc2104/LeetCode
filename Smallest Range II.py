# https://leetcode.com/problems/smallest-range-ii/
# https://leetcode.com/problems/smallest-range-ii/solutions/173377/c-java-python-add-0-or-2-k/

# greedy, TC:O(NlogN), SC:O(N) for timsort
def smallestRangeII(nums: List[int], k: int) -> int:
    nums.sort()
    m, M = nums[0] + k, nums[-1] - k  # possible min and max candidates cause smallest score
    res = nums[-1] - nums[0]
    for i in range(len(nums) - 1):
        # find other possibility
        new_min = nums[i + 1] - k  # bigger minus k
        new_max = nums[i] + k  # smaller plus k
        res = min(res, max(M, new_max) - min(m, new_min))
    return res


# greedy, TC:O(NlogN), SC:O(N) for timsort
def smallestRangeII2(nums: List[int], k: int) -> int:
    nums.sort()
    res = nums[-1] - nums[0]
    for i in range(len(nums)-1):
        # find other possibility
        new_max = max(nums[i] + 2*k, nums[-1])
        new_min = min(nums[i+1], nums[0] + 2*k)
        res = min(res, new_max - new_min) # we choose +0k or +2k
    return res