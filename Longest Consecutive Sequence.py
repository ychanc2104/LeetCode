# https://leetcode.com/problems/longest-consecutive-sequence/


# brute force, TC: O(n^3)
def longestConsecutive(nums) -> int:
    res = 0
    # brute force
    # O(n)
    for i in range(len(nums)):
        num = nums[i]
        ans = 1
        # O(n^2), O(n) for num+1 in nums and O(n) for while loop
        while num + 1 in nums:
            ans += 1
            num += 1
        res = max(res, ans)
    return res

# TC: O(n)
def longestConsecutive2(nums) -> int:
     # [100,4,200,1,3,2]
    res = 0
    nums_set = set(nums)  # small to big
    for num in nums_set:
        # do not start if num is not head
        if num - 1 in nums_set:
            continue
        # main loop to get res, start from 1
        ans = 1
        while num + 1 in nums_set:
            ans += 1
            num += 1
        res = max(ans, res)
    return res

nums = [100,4,200,1,3,2,0,6,5,7,8]
res = longestConsecutive(nums)
