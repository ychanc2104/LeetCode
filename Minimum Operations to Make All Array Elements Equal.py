# https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/

# TC:O(NlogN +MlogN), SC:O(N)
def minOperations(nums: List[int], queries: List[int]) -> List[int]:
    res = []
    nums.sort()
    prefix = []
    s = 0
    for num in nums:
        s += num
        prefix.append(s)

    def bsearch(target):
        L, R = 0, len(nums ) -1
        while L <= R:
            mid = ( L +R )/ /2
            if nums[mid] <= target:
                L = mid + 1
            else:
                R = mid - 1
        return L
    n = len(nums)
    for q in queries:
        idx = bsearch(q)

        if idx == len(nums):
            res.append( q *n - prefix[-1])
        elif idx == 0:
            res.append(prefix[-1] - n* q)
        else:
            res.append((idx) * q - prefix[idx - 1] + (prefix[-1] - prefix[idx - 1]) - (len(nums) - idx) * q)
    return res

# TC:O(NlogN +MlogN), SC:O(N)
def minOperations2(nums: List[int], queries: List[int]) -> List[int]:
    res = []
    nums.sort()
    prefix = [0]
    s = 0
    for num in nums:
        s += num
        prefix.append(s)

    def bsearch(target):
        L, R = 0, len(nums) - 1
        while L <= R:
            mid = (L + R) // 2
            if nums[mid] <= target:
                L = mid + 1
            else:
                R = mid - 1
        return L

    n = len(nums)
    for q in queries:
        idx = bsearch(q)
        l = (idx) * q - prefix[idx]
        r = (prefix[-1] - prefix[idx]) - (n - idx) * q

        res.append(l + r)
    return res