# https://leetcode.com/problems/binary-search/
# https://leetcode.com/problems/binary-search/discuss/423162/Binary-Search-101

# TC: O(logn),
def search(nums, target) -> int:
    L, R = 0, len(nums) - 1
    while L <= R:
        mid = L + (R - L) // 2 # prevent overflow
        if nums[mid] > target:
            R = mid - 1
        elif nums[mid] < target:
            L = mid + 1
        else:
            return mid
    return -1


# prevent overflow
def search2(nums, target) -> int:
    L, R = 0, len(nums)-1
    while L <= R:
        mid = (L+R)>>1
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            R = mid - 1
        else:
            L = mid + 1
    return -1