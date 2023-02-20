# https://leetcode.com/problems/first-missing-positive/
# https://leetcode.com/problems/first-missing-positive/discuss/872448/Python-O(n)-solution-with-constant-space-EXPLAINED-with-clear-train-of-thoughts
# https://leetcode.com/problems/first-missing-positive/discuss/17080/Python-O(1)-space-O(n)-time-solution-with-explanation


# use num as index, TC:O(n), SC:O(n)
def firstMissingPositive(nums) -> int:
    # answer must be between 1 and n+1
    n = len(nums)
    # clean data
    for i in range(n):
        if nums[i] > n:
            nums[i] = 0

    flags = [True] * n
    for num in nums:
        if 0 < num:  # ignore negative
            flags[(num - 1) % n] = False

    for i in range(n):
        if flags[i]:
            return i + 1
    return n + 1


# TC:O(n), SC:O(1)
def firstMissingPositive2(nums) -> int:
    # answer must be between 1 and n+1
    n = len(nums)
    # clean data, make all data is between 0 and n
    for i in range(n):
        if nums[i] > n or nums[i] < 0:
            nums[i] = 0
    # index i means does i+1 appear
    for num in nums:
        index = (num) % (n+1) - 1 # 0 to n-1
        if num > 0 and index >= 0: # ignore negative and zero, and index < 0
            # prevent affect the index not used
            nums[(num) % (n+1) - 1] += n+1 # add n+1 to prevent original position is 0
    #print(nums)
    for i in range(n):
        if nums[i] <= n:
            return i+1
    return n+1

# TC:O(n), SC:O(1)
def firstMissingPositive3(nums) -> int:
    # if len(nums) is N, answer must in [1,N+1]
    n = len(nums)
    flagN = False
    for i, num in enumerate(nums):
        if num < 0 or num >= n:
            nums[i] = 0
            if num == n:
                flagN = True
    # print(nums)
    for i, num in enumerate(nums):
        nums[(num) % (n + 1)] += n + 1

    for i in range(1, n):  # check answer from 1 to n-1
        if nums[i] < n:
            return i
    return n + 1 if flagN else n  # check n and n+1