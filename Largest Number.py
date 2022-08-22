# https://leetcode.com/problems/largest-number/
# https://leetcode.com/problems/largest-number/discuss/53298/Python-different-solutions-(bubble-insertion-selection-merge-quick-sorts).
# https://leetcode.com/problems/largest-number/discuss/863489/Python-2-lines-solution-using-sort-explained

import functools

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

# use in-place quick sort, TC:O(nlogn), SC:O(logn)
def largestNumber2(nums) -> str:
    def quick_sort(L, R):
        def partition(L, R):
            pivot = str(nums[R])
            for i in range(L, R):
                num = str(nums[i])
                # move bigger to L
                if pivot + num <= num + pivot:
                    nums[i], nums[L] = nums[L], nums[i]
                    L += 1
            nums[L], nums[R] = nums[R], nums[L]
            return L

        if L >= R: return
        pos = partition(L, R)
        quick_sort(L, pos - 1)
        quick_sort(pos + 1, R)

    quick_sort(0, len(nums) - 1)
    print(nums)
    return ''.join([str(num) for num in nums]) if nums[0] != 0 else "0"

# timsort, TC:O(nlogn), SC:O(n)
def largestNumber3(nums) -> str:
    # compare str(x)+str(y) bigger return -1 (ascending order)
    nums.sort(key=functools.cmp_to_key(lambda x, y: -1 if str(x) + str(y) > str(y) + str(x) else 1))
    # print(nums)
    return ''.join([str(num) for num in nums]) if nums[0] != 0 else "0"