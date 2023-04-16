# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/


# binary search, TC:(logN), SC:O(1)
def peakIndexInMountainArray(arr: List[int]) -> int:
    L, R = 0, len(arr) - 1
    while L <= R:
        mid = (L + R) // 2
        if arr[mid] >= arr[mid + 1]:  # must exist a peak (mid must not go to n-1)
            R = mid - 1
        else:
            L = mid + 1
    return L