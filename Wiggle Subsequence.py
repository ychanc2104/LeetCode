# https://leetcode.com/problems/wiggle-subsequence/description/
# https://leetcode.com/problems/wiggle-subsequence/solutions/84843/easy-understanding-dp-solution-with-o-n-java-version/


# dp, TC:O(N), SC:O(N)
def wiggleMaxLength(nums: List[int]) -> int:
    n = len(nums)
    up = [0] * n  # end with increasing, up[i]: max wiggle sequence end with increasing in [0, i]
    down = [0] * n  # end with decreasing, down[i]: max wiggle sequence end with decreasing in [0, i]
    up[0] = 1
    down[0] = 1
    for i in range(1, n):
        if nums[i] > nums[i - 1]:  # incraseing
            up[i] = down[i - 1] + 1
            down[i] = down[i - 1]
        elif nums[i] < nums[i - 1]:  # decreasing
            up[i] = up[i - 1]
            down[i] = up[i - 1] + 1
        else:
            up[i] = up[i - 1]
            down[i] = down[i - 1]
    return max(up[-1], down[-1])


# space optimized dp, TC:O(N), SC:O(1)
def wiggleMaxLength(nums: List[int]) -> int:
    n = len(nums)

    up = 1
    down = 1
    for i in range(1, n):
        if nums[i] > nums[i-1]: # incraseing
            up = down + 1
        elif nums[i] < nums[i-1]: # decreasing
            down = up + 1
    return max(up, down)