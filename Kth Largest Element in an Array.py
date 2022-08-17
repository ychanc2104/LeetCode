# https://leetcode.com/problems/kth-largest-element-in-an-array/
# https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/1019513/Python-QuickSelect-average-O(n)-explained


import random


# quick select, TC:O(n) in average, O(n^2) in worst case, SC:O(1)
def findKthLargest(nums, k: int) -> int:
    def partition(L, R):
        pivot = random.randint(L, R)
        target = nums[pivot]
        # move pivot to R
        nums[R], nums[pivot] = nums[pivot], nums[R]
        # move all num>=target to the left
        for i in range(L, R):
            if nums[i] >= target:
                nums[i], nums[L] = nums[L], nums[i]
                L += 1
        # move pivot to L
        nums[L], nums[R] = nums[R], nums[L]
        # 0~L-1 are all greater than L
        return L

    L, R = 0, len(nums) - 1
    while L < R:
        # L~pivot-1 are greater than pivot
        pivot = partition(L, R)
        if pivot < k:  # don't use <=
            # move L to right
            L = pivot + 1
        # elif pivot + 1 == k:
        #     return nums[k - 1]
        else:
            # move R to left
            R = pivot - 1
    return nums[k - 1]

# recursive quick sort, TC:O(n) in average, O(n^2) in worst case, SC:O(n)
def findKthLargest2(nums, k: int) -> int:
    if not nums: return
    pivot = random.choice(nums)
    left = [x for x in nums if x > pivot]
    mid = [x for x in nums if x == pivot]
    right = [x for x in nums if x < pivot]

    L, M = len(left), len(mid)

    if k <= L:
        return findKthLargest2(left, k)
    elif k > L + M:
        return findKthLargest2(right, k - L - M)
    else:
        return mid[0]