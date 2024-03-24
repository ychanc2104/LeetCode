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

# modified nums, TC:O(n), SC:O(1)
def findDuplicate3(nums) -> int:
    while nums[0] != nums[nums[0]]:
        # swap
        nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
        print(nums)
    return nums[0]

# count and binary search, TC:O(nlogn), SC:O(1)
def findDuplicate4(nums) -> int:
    def count(mid):
        return len([num for num in nums if num <= mid])

    L, R = 0, len(nums) - 1
    while L <= R:
        mid = (L + R) // 2
        if count(mid) > mid:
            R = mid - 1
        else:
            L = mid + 1
    return L


nums = [1,3,4,2,2]
res3 = findDuplicate3(nums)