class Solution:
    def __init__(self, nums, target):
        self.ans_1 = self.twoSum_1(nums, target)
        self.ans_2 = self.twoSum_2(nums, target)

    def twoSum_1(self, nums, target):
        x = dict()
        for i in range(len(nums)):
            if nums[i] not in x.keys():
                x[nums[i]] = i
            value = target - nums[i]
            if value in x.keys() and i != x.get(value):
                return [x.get(value), i] ## directly exit loop while using return

    def twoSum_2(self, nums, target):
        n = len(nums)
        i=0
        output = []
        while output==[]:
            for j in range(n-1-i):
                if nums[i] + nums[j+i+1] == target:
                    output = [i, i+j+1]
                    return output
            i += 1
    ## T: O(n)
    def twoSum_3(self, nums, target):
        memo = {}
        for i,num in enumerate(nums):
            if num not in memo:
                memo[target-num] = i
            else:
                return [memo[num], i]
nums = [3,2,4,1,9,7]
target = 11

A = Solution(nums, target)
