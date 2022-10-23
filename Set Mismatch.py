# https://leetcode.com/problems/set-mismatch/description/
# https://leetcode.com/problems/set-mismatch/solutions/1089732/python-o-1-space-o-n-time-tricky-super-simple/?orderBy=most_votes&languageTags=python


# first thought, TC:O(N), SC:O(N)
def findErrorNums(nums: List[int]) -> List[int]:
    # find duplicate and missing number
    # range from 1 to n
    product = 0
    memo = set()
    for i, num in enumerate(nums, 1):
        product ^= i ^ num
        if num in memo:
            dup = num
        else:
            memo.add(num)
    missing = product ^ dup
    return [dup, missing]

# TC:O(N), SC:O(1)
def findErrorNums2(nums: List[int]) -> List[int]:
    # find duplicate and missing number
    # range from 1 to n, not sorted
    product = 0
    for i,num in enumerate(nums, 1):
        product ^= i^abs(num)
        if nums[abs(num)-1] < 0:
            dup = abs(num)
        else:
            nums[(abs(num) - 1)] *= -1
    missing = product ^ dup
    return [dup, missing]
