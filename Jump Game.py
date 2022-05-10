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





def canJump3(nums):
    step = nums[0]
    target = len(nums) - 1
    if step >= target:
        return True
    elif step == 0:
        return False
    else:
        index = [i + num for i, num in enumerate(nums[1:step + 1])].index(
            max([i + num for i, num in enumerate(nums[1:step + 1])]))
        res = canJump3(nums[index + 1:])
        if res:
            return res
    return False



nums = [2,0,1,1,1,1,1,2,0,3,0,0,2,0,4]

res = canJump(nums)
res2 = canJump3(nums)
