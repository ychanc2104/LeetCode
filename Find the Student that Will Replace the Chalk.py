# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/?envType=study-plan&id=binary-search-ii

# binary search + prefix sum, TC:O(N), SC:O(N)
def chalkReplacer(chalk: List[int], k: int) -> int:
    tempSum = 0
    prefixSum = []
    for c in chalk:
        tempSum += c
        prefixSum.append(tempSum)
    k %= tempSum
    L, R = 0, len(prefixSum) - 1
    while L <= R:  # leftmost
        mid = (L + R) // 2
        if prefixSum[mid] == k:
            return mid + 1
        elif prefixSum[mid] > k:
            R = mid - 1
        else:
            L = mid + 1
    return L

# simple linear scan, TC:O(N), SC:O(1)
def chalkReplacer2(chalk: List[int], k: int) -> int:
    k %= sum(chalk) # O(N)
    for i in range(len(chalk)):
        k -= chalk[i]
        if k < 0:
            return i