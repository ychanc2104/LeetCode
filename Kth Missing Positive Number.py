# https://leetcode.com/problems/kth-missing-positive-number/description/

# binary search, TC:O(logN), SC:O(1)
def findKthPositive(arr: List[int], k: int) -> int:
    L, R = 0, len(arr) - 1
    while L <= R:
        mid = (L + R) // 2
        if arr[mid] - mid - 1 >= k:  # too many missing, move left
            R = mid - 1
        else:
            L = mid + 1
    return L + k