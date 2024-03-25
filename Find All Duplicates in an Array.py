# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/?envType=daily-question&envId=2024-03-25


# TC:O(N), SC:O(1)
def findDuplicates(nums: List[int]) -> List[int]:
    res = []
    for num in nums:
        num_abs = abs(num)
        if nums[num_abs - 1] < 0:  # visited
            res.append(num_abs)
        nums[num_abs - 1] *= -1
    return res