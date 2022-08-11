# https://leetcode.com/problems/binary-search/
# https://medium.com/appworks-school/binary-search-%E9%82%A3%E4%BA%9B%E8%97%8F%E5%9C%A8%E7%B4%B0%E7%AF%80%E8%A3%A1%E7%9A%84%E9%AD%94%E9%AC%BC-%E4%B8%80-%E5%9F%BA%E7%A4%8E%E4%BB%8B%E7%B4%B9-dd2cd804aee1

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


# leftmost binary search
def search_leftmost(nums, target) -> int:
    L, R = 0, len(nums)
    while L < R:
        mid = L + (R-L)//2
        if nums[mid] >= target:
            R = mid
        else:
            L = mid + 1
    return L

def search_leftmost2(nums, target) -> int:
    L, R = 0, len(nums)-1
    res = -1
    while L <= R:
        mid = L + (R-L)//2
        if nums[mid] > target:
            R = mid - 1
        elif nums[mid] < target:
            L = mid + 1
        else:
            R = mid - 1
            res = mid
    return res


def search_leftmost3(nums, target) -> int:
    L, R = 0, len(nums)-1
    while L <= R:
        mid = L + (R-L)//2
        if nums[mid] >= target:
            R = mid - 1
        else:
            L = mid + 1
    return L

def search_rightmost(nums, target) -> int:
    L, R = 0, len(nums)
    while L < R:
        mid = L + (R-L)//2
        if nums[mid] > target:
            R = mid
        else:
            L = mid + 1
    return R-1

def search_rightmost2(nums, target) -> int:
    L, R = 0, len(nums) - 1
    res = -1
    while L <= R:
        mid = L + (R-L)//2
        if nums[mid] > target:
            R = mid - 1
        elif nums[mid] < target:
            L = mid + 1
        else:
            res = mid
            L = mid + 1
    return res


def search_rightmost3(nums, target) -> int:
    L, R = 0, len(nums) - 1
    while L <= R:
        mid = L + (R-L)//2
        if nums[mid] <= target:
            L = mid + 1
        else:
            R = mid - 1
    return R

nums = [1,1,1,1,2,2,2,3,3,4,5,5,5]
target = 1
res = search_leftmost(nums, target)
res2 = search_leftmost2(nums, target)
res3 = search_leftmost3(nums, target)

res4 = search_rightmost(nums, target)
res5 = search_rightmost2(nums, target)
res6 = search_rightmost3(nums, target)