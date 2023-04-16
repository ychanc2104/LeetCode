# https://leetcode.com/problems/minimize-maximum-of-array/description/
# https://leetcode.com/problems/minimize-maximum-of-array/solutions/2706375/binary-search-with-explanation/


# binary search, TC:O(MlogN), M is max number in nums, SC:O(1)
def minimizeArrayValue(nums: List[int]) -> int:
    def check(nums, criteria):
        # make all nums is <= criteria
        compensate = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] + compensate > criteria:
                compensate += nums[i] - criteria
            else:
                compensate = 0
        return nums[0] + compensate <= criteria

    # 1,7 4  5,7 6  5,5 5
    L, R = 0, max(nums)
    while L <= R:
        # print(nums)
        mid = (L + R) // 2
        if check(nums, mid):  # try smaller
            R = mid - 1
        else:
            L = mid + 1
    return L

# greedy, TC:O(N), SC:O(1)
def minimizeArrayValue2(nums: List[int]) -> int:

    s = sum(nums)
    res = 0
    for i in range(len(nums) - 1, -1, -1):
        # res = max(res, math.ceil(s / (i + 1)))
        res = max(res, (s+i)//(i+1)) # upper bound, calculate average
        s -= nums[i]
    return res