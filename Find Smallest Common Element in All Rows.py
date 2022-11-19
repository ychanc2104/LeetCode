# https://leetcode.com/problems/find-smallest-common-element-in-all-rows/

import collections

# use counter because no duplicate in each row(strictly increasing), TC:O(NM), SC:O(k) k is range of constrained values
def smallestCommonElement(mat) -> int:
    n, m = len(mat), len(mat[0])
    counter = collections.Counter()
    for row in mat:
        for value in row:
            counter[value] += 1
    res = -1
    for value, count in counter.items():
        if count == n and (res == -1 or value < res):
            res = value
    return res

# modified 1, TC:O(NM), SC:O(k) => handle duplicates,
def smallestCommonElement2(mat) -> int:
    n, m = len(mat), len(mat[0])
    counter = collections.Counter()
    for row in mat:
        for value in row:
            counter[value] += 1
            if counter[value] == n: # meet solution already
                return value
    return -1


# modified 1 + handle duplicates, TC:O(NM), SC:O(k)
def smallestCommonElement3(mat) -> int:
    n, m = len(mat), len(mat[0])
    counter = collections.Counter()
    for row in mat:
        prev_value = float("inf")
        for value in row:
            if value == prev_value:
                continue
            prev_value = value
            counter[value] += 1
            if counter[value] == n: # meet solution already
                return value
    return -1

# use set,
def smallestCommonElement4(mat) -> int:
    S = set(mat[0])
    for i in range(1, len(mat)):
        S = S.intersection(mat[i])
    return -1 if not S else min(S)

# binary search, TC:O(NMlogM), SC:O(1)
def smallestCommonElement5(mat) -> int:

    def binary_search(nums, target):
        L, R = 0, len(nums)-1
        while L <= R:
            mid = (L + R) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                R = mid - 1
            else:
                L = mid + 1
        return False # not found

    n, m = len(mat), len(mat[0])
    for j in range(m):
        status = True
        target = mat[0][j] # from small to big
        for i in range(1, n):
            status = binary_search(mat[i], target)
            if not status: break # not found
        if status: # or use else:
            return target
    return -1

mat_d = [[1,2,3,4,5],[5,7,7,7,7],[5,7,7,7,7],[1,2,4,4,5],[1,2,4,4,5]]
res_d = smallestCommonElement3(mat_d)