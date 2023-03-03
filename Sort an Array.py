# https://leetcode.com/problems/sort-an-array/description/
# https://leetcode.com/problems/sort-an-array/solutions/492042/7-sorting-algorithms-quick-sort-top-down-bottom-up-merge-sort-heap-sort-etc/


import random

# first thought, quick sort, TC:O(NlogN) and O(N^2) for worst, SC:O(N)
def sortArray(nums: List[int]) -> List[int]:
    def partition(L, R):
        pivot = random.randint(L, R)
        nums[pivot], nums[R] = nums[R], nums[pivot]
        # make [L,pivot] is greater than nums[pivot]
        for i in range(L, R):
            if nums[i] <= nums[R]:
                nums[i], nums[L] = nums[L], nums[i]
                L += 1
        nums[L], nums[R] = nums[R], nums[L]
        return L

    def quick_sort(L, R):
        if L >= R:
            return
        idx = partition(L, R)
        quick_sort(L, idx - 1)
        quick_sort(idx + 1, R)

    quick_sort(0, len(nums) - 1)
    return nums



# merge sort, TC:O(NlogN) for worst, SC:O(N)
def sortArray2(nums: List[int]) -> List[int]:

    def merge_sort(L, R):
        if L == R:
            return [nums[L]]
        mid = (L+R)//2
        left = merge_sort(L, mid)
        right = merge_sort(mid+1, R)
        #merge
        i, j = 0, 0
        merge = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merge.append(left[i])
                i += 1
            else:
                merge.append(right[j])
                j += 1
        if i < len(left):
            merge.extend(left[i:])
        else:
            merge.extend(right[j:])
        return merge

    return merge_sort(0, len(nums)-1)