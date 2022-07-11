# https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    ## inf idea
    def search(self, nums, target):
        L, H = 0, len(nums)
        while L < H:
            M = (L+H) // 2
            if target < nums[0] < nums[M]: # -inf
                ## to the right
                L = M+1
            elif target >= nums[0] > nums[M]: # +inf
                ## to the left
                H = M
            elif nums[M] < target:
                ## to the right
                L = M+1
            elif nums[M] > target:
                ## to the left
                H = M
            else:
                return M
        return -1
    ## four cases
    def search2(self, nums, target):
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

    def search3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # if found target value, return the index
            if nums[mid] == target:
                return mid

            # determine it's left rotated or right rotated
            """
            No rotated:
            1 2 3 4 5 6 7
                 mid

            left rotated: pivot at the left side of the origin sorted array, A[mid] >= A[left]
            3 4 5 6 7 1 2
                 mid
            search in A[left] ~ A [mid] if A[left] <= target < A[mid] else, search right side

            right rotated: pivot at the right side of the origin sorted array, A[mid] < A[left]
            6 7 1 2 3 4 5
                 mid          
            search in A[mid] ~ A[right] if A[mid] < target <= A[right] else, search left side
            """
            if nums[mid] >= nums[left]:  # left rotated
                # in ascending order side
                if nums[left] <= target and target < nums[mid]:
                    # if nums[L] == target, go left until L = R = 0
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # right rotated
                # in ascending order side
                if nums[mid] < target and target <= nums[right]:
                    # if nums[R]==target, go right until L = R = len(nums)-1
                    left = mid + 1
                else:
                    right = mid - 1
        # cannot find the target value
        return -1