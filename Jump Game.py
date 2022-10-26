# https://leetcode.com/problems/jump-game/
# https://leetcode.com/problems/jump-game/discuss/20907/1-6-lines-O(n)-time-O(1)-space
#
from functools import reduce


def canJump(nums):
    reach = 0
    for i, num in enumerate(nums):
        if reach >= len(nums) - 1:
            return True
        elif reach < i:
            return False
        elif i + num > reach:
            reach = i + num
    return True

# greedy, TC:O(n), SC:O(1)
def canJump2(nums):
    reach = nums[0]
    for i in range(1, len(nums)):
        if i > reach:
            return False
        reach = max(reach, i + nums[i])
    return True




nums = [2,0,1,1,1,1,1,2,0,3,0,0,2,0,4]

res = canJump(nums)
res2 = canJump3(nums)
