# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/158940/Beat-100%3A-Very-Simple-(Python)-Very-Detailed-Explanation

# neetcode
def findMin(nums) -> int:
    res = nums[0]
    L, R = 0, len(nums) - 1

    while L <= R:
        ## already in sorted portion, [4,5,6,7,0,1,2] will fail
        if nums[L] < nums[R]:
            res = min(res, nums[L])
            break

        mid = (L + R) // 2
        # print(L, mid, R, res)
        res = min(res, nums[mid])
        if nums[mid] >= nums[L]:
            L = mid + 1
        elif nums[mid] < nums[L]:
            R = mid - 1
        # print(L, mid, R, res)
    return res

def findMin2(nums) -> int:
    L, R = 0, len(nums) - 1
    ## end loop when L==R
    while L < R:
        mid = (L + R) // 2
        # print(L, mid, R, res)
        if nums[mid] > nums[R]:
            L = mid + 1
        elif nums[mid] <= nums[R]:  # min in the left or self
            R = mid
        # print(L, mid, R, res)
    return nums[L]

nums = [3,4,5,1,2]

res = findMin(nums)