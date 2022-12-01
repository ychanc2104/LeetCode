# https://leetcode.com/problems/frequency-of-the-most-frequent-element/
# https://leetcode.com/problems/frequency-of-the-most-frequent-element/solutions/1175028/python-binary-search-prefix-sums/
# https://leetcode.com/problems/frequency-of-the-most-frequent-element/solutions/1175090/java-c-python-sliding-window/


# sliding window, TC:O(nlogn) for sorting, SC:O(N) for timsort
def maxFrequency(nums: List[int], k: int) -> int:
    # [1,5,13,26] k+sum() >= size*max
    nums.sort()
    res = 1
    L = 0
    S = 0
    for R in range(len(nums)):
        S += nums[R]
        # increase L size
        while S + k < (R + 1 - L) * nums[R]:  # invalid window
            S -= nums[L]
            L += 1
        res = max(res, R - L + 1)
    return res


# binary search (TLE), TC:O(nlogn), SC:O(N)
def maxFrequency2(nums: List[int], k: int) -> int:
    def bsearch(prefix, M):
        n = len(prefix)
        L, R = 0, n-1 # prefix sum
        while L <= R:
            mid = (L + R)//2
            if k + prefix[-1] - prefix[mid] + M >= (n-mid)*M: # valid, expand(not include mid)
                R = mid - 1
            else:
                L = mid + 1
        return L
    # [1,5,13,26] k+sum() >= size*max
    nums.sort()
    prefix = [0]
    res = 1
    for i in range(len(nums)):
        # binary search to find valid leftmost index at given i
        idx = bsearch(prefix, nums[i])
        prefix.append(prefix[-1] + nums[i])
        # increase L size
        res = max(res, i-idx+1)
    return res