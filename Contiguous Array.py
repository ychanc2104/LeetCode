# https://leetcode.com/problems/contiguous-array/

# hashtable, TC:O(n), SC:O(n)
def findMaxLength(nums) -> int:
    # find max length when array contains equal number of 0 and 1
    # encounter 0 => -1, encounter 1 => +1
    memo = {0: -1}  # important to assign initial value, ex: [0,1]
    count = 0
    res = 0
    for i, num in enumerate(nums):
        if num == 0:
            count -= 1
        else:
            count += 1
        if count in memo:
            res = max(res, i - memo[count])
        else:
            memo[count] = i
    # print(memo)
    return res

# hashtable + prefix sum, TC:O(n), SC:O(n)
def findMaxLength2(nums: List[int]) -> int:
    # 0:-1, 1:+1
    memo = {0:-1, 1:1}
    prefix = {0:-1}
    n = len(nums)
    res = 0
    s = 0
    for i in range(n):
        target = s + memo[nums[i]]
        if target in prefix: # s - prefix[x] + memo[nums[i]] = 0, valid in [x+1,i]
            res = max(res, i - prefix[target])
        s += memo[nums[i]]
        if s not in prefix:
            prefix[s] = i
    return res