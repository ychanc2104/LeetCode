# https://leetcode.com/problems/find-the-duplicate-number/
# https://leetcode.com/problems/find-the-duplicate-number/discuss/72846/My-easy-understood-solution-with-O(n)-time-and-O(1)-space-without-modifying-the-array.-With-clear-explanation.

# TC:O(n), SC:O(1)
def findDuplicate(nums) -> int:
    # let num as index
    for num in nums:
        if nums[abs(num)] < 0:
            # visit twice
            res = abs(num)
            break
        nums[abs(num)] = -nums[abs(num)]
    # recover
    for i in range(len(nums)):
        nums[i] = abs(nums[i])
    return res


# two pointer, TC:O(n), SC:O(1)
def findDuplicate2(nums) -> int:
    # two pointers
    # meet at cycle, we have 2d(fast) = d(slow) => 2(F+a) = F+a+nC
    # F+a = nC, n = 1,2,3,...,n
    slow = nums[0]
    fast = nums[slow]
    while slow!=fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    # find the entry point (duplicate number)
    # F = C-a, starting from 0, the intersection must be the duplicate number
    fast = 0
    while slow!=fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

