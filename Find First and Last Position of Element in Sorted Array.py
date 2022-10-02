# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/


def searchRange(nums, target: int):
    if not nums: return [-1, -1]

    # find leftmost
    def bsearch_l(nums, target):
        L, R = 0, len(nums) - 1
        while L <= R:
            mid = L + (R - L) // 2
            if nums[mid] >= target:
                # move R
                R = mid - 1
            else:
                L = mid + 1
        return L if L < len(nums) and nums[L] == target else -1

    # find rightmost
    def bsearch_r(nums, target):
        L, R = 0, len(nums) - 1
        while L <= R:
            mid = L + (R - L) // 2
            if nums[mid] <= target:
                # move L
                L = mid + 1
            else:
                R = mid - 1
        return R if R>=0 and nums[R] == target else -1

    return [bsearch_l(nums, target), bsearch_r(nums, target)]