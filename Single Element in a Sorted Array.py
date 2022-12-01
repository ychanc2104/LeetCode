# https://leetcode.com/problems/single-element-in-a-sorted-array/


# binary search, TC:O(logN), SC:O(1)
def singleNonDuplicate(nums: List[int]) -> int:
    L, R = 0, len(nums) - 1
    while L < R:  # stop when L == R
        mid = (L + R) // 2
        if nums[mid - 1] == nums[mid]:
            if (mid - 1 - L) & 1:  # odd number, move R
                R = mid - 1 - 1  # (mid-1) is already checked
            else:
                L = mid + 1
        elif nums[mid + 1] == nums[mid]:
            if (R - (mid + 1)) & 1:  # odd number, move L
                L = mid + 1 + 1  # (mid+1) is already checked
            else:
                R = mid - 1
        else:
            return nums[mid]  # must exist
    return nums[L]