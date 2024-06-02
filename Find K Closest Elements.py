# https://leetcode.com/problems/find-k-closest-elements/
# https://leetcode.com/problems/find-k-closest-elements/discuss/462664/Python-binary-search-with-detailed-explanation
# https://leetcode.com/problems/find-k-closest-elements/discuss/301797/Python-O(log(N-K)-%2B-K)-Binary-Search-W-left-less-right

# use two pointers, TC:O(n), SC:O(1)
def findClosestElements(arr, k: int, x: int):
    L, R = 0, len(arr) - 1

    while R - L + 1 != k:
        if abs(arr[L] - x) <= abs(arr[R] - x):
            # L is closer
            R -= 1
        elif abs(arr[L] - x) > abs(arr[R] - x):
            # R is closer
            L += 1
    return arr[L:R + 1]

# leftmost binary search, TC:O(log(n-k)+k), SC:O(1)
def findClosestElements2(arr, k: int, x: int):
    L, R = 0, len(arr) - k  # let L can reach len(arr)-k => R = mid
    # to find the leftmost num of answer array
    # TC:O(log(n-k))
    while L < R:
        mid = L + (R - L) // 2
        if x - arr[mid] <= arr[mid + k] - x:
            # mid is closer, go to left
            R = mid
        else:
            # mid+k is closer, go to right
            L = mid + 1
    # array slice, TC:O(k)
    return arr[L:L + k]

# leftmost binary search, TC:O(log(n-k)+k), SC:O(1)
def findClosestElements3(arr, k: int, x: int):
    L, R = 0, len(arr) - 1 - k
    # to find the leftmost num of answer array
    # TC:O(log(n-k))
    while L <= R:
        mid = L + (R - L) // 2
        if x - arr[mid] <= arr[mid + k] - x:
            # mid is closer, go to left
            # equal => move R to preserve L
            R = mid - 1
        else:
            # mid+k is closer, go to right
            # L never reach the target until L>R => L is the answer
            L = mid + 1
    # array slice, TC:O(k)
    return arr[L:L + k]

def findClosestElements4(arr: List[int], k: int, x: int) -> List[int]:
    L, R = k, len(arr) - 1
    while L <= R:
        mid = (L + R) // 2
        if arr[mid] - x + arr[mid - k] - x >= 0:
            R = mid - 1
        else:
            L = mid + 1

    return arr[L - k:L]