class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        s = sum(nums)
        s2 = int(n*(n+1)/2)
        diff = s2-s
        return diff