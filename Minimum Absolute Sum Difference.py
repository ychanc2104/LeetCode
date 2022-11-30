# https://leetcode.com/problems/minimum-absolute-sum-difference/
# https://leetcode.com/problems/minimum-absolute-sum-difference/solutions/1141382/clean-python-3-binary-search/

# binary search, TC:O(NlogN), SC:O(N)
def minAbsoluteSumDiff(nums1: List[int], nums2: List[int]) -> int:
    def bsearch(nums, target):
        L, R = 0, len(nums) - 1
        while L <= R:
            mid = (L + R) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                R = mid - 1
            else:
                L = mid + 1
        return L # must be bigger than target

    # find max decrease of any pair, using num2[i] to find any element in nums1
    # one pass
    sumDiff = sum(abs(x - y) for x, y in zip(nums1, nums2))
    gain = 0
    nums1_sort = sorted(nums1)  # sort and do binary search
    for i in range(len(nums1)):
        idx = bsearch(nums1_sort, nums2[i])
        if idx > 0:  # its neighbor
            gain = max(gain, abs(nums1[i] - nums2[i]) - abs(nums1_sort[idx - 1] - nums2[i]))
        if idx < len(nums1):
            gain = max(gain, abs(nums1[i] - nums2[i]) - abs(nums1_sort[idx] - nums2[i]))
    return (sumDiff - gain) % (10 ** 9 + 7)