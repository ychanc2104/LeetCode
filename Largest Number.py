# https://leetcode.com/problems/largest-number/



# use custom sorting, TC:O(nlogn), SC:O(n)
def largestNumber(nums) -> str:
    def quick_sort(nums):
        if not nums:
            return []
        pivot = str(nums[0])
        L = []
        R = []
        # move big num to L
        for num in nums[1:]:
            num = str(num)
            if num + pivot >= pivot + num:
                L.append(num)
            else:
                R.append(num)
        return quick_sort(L) + [pivot] + quick_sort(R)
    nums = quick_sort(nums)
    return ''.join(nums) if nums[0]!="0" else "0"