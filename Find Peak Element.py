# https://leetcode.com/problems/find-peak-element/


# TC:O(), SC:O()
def findPeakElement(nums: List[int]) -> int:
    nums = [float('-inf')] + nums + [float('-inf')]
    n = len(nums)

    def helper(L, R):
        if L > R:
            return None
        mid = (L + R) // 2
        if nums[mid - 1] < nums[mid] > nums[mid + 1]:
            return mid
        left = helper(L, mid - 1)
        if left:
            return left
        right = helper(mid + 1, R)
        if right:
            return right
        return None

    return helper(1, len(nums) - 2) - 1

# TC:O(N), SC:O(1)
def findPeakElement(nums: List[int]) -> int:

    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            # imply nums[i-1] < nums[i] also
            return i
    return len(nums) - 1


# binary search, TC:O(logN), SC:O(1)
def findPeakElement2(nums: List[int]) -> int:
    # 1,2,3,4,5
    n = len(nums)
    L, R = 0, n-1
    while L <= R:
        mid = (L + R)//2
        if nums[mid] >= nums[min(mid + 1, n-1)]: # if equal => same number
            # check left
            R = mid - 1
        else:
            L = mid + 1
    return L