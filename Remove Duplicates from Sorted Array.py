# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# first thought, TC:O(N), SC:O(N)
def removeDuplicates(nums) -> int:
    memo = {}
    for num in nums:
        memo[num] = memo.get(num, 0) + 1
    for i, key in enumerate(memo.keys()):
        nums[i] = key
    return i + 1

# TC:O(N), SC:O(1)
def removeDuplicates2(nums) -> int:
    # two pointer, L to each k position, R to find swapped number
    L = 1
    last_num = nums[0]
    for R in range(1, len(nums)):
        if nums[R] != last_num:
            last_num = nums[R]
            nums[L], nums[R] = nums[R], nums[L]
            L += 1
    return L


# TC:O(N), SC:O(1)
def removeDuplicates3(nums) -> int:
    size = len(nums)
    insertIndex = 1
    for i in range(1, size):
        # Found unique element
        if nums[i - 1] != nums[i]:
            # Updating insertIndex in our main array
            nums[insertIndex] = nums[i]
            # Incrementing insertIndex count by 1
            insertIndex = insertIndex + 1
    return insertIndex