# https://leetcode.com/problems/valid-triangle-number/description/?envType=study-plan&id=binary-search-ii

# first thought, TC:O(N^2logN), SC:O(N) for timsort
def triangleNumber(nums: List[int]) -> int:
    # a + b > c for any edge
    nums.sort()
    res = 0
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            # do binary search to find last
            target = nums[i] + nums[j]  # find last element is smaller than target
            L, R = j + 1, len(nums) - 1
            while L <= R:
                mid = (L + R) // 2
                if nums[mid] >= target:
                    R = mid - 1
                else:
                    L = mid + 1
            # use L-1, 1,1,3,3,5
            res += (L - 1) - j
    return res

# two pointers, TC:O(N^2), SC:O(N) for timsort
def triangleNumber2(nums: List[int]) -> int:
    # a + b > c for any edge
    nums.sort()
    res = 0
    for i in range(len(nums) - 1, 1, -1):  # n-1 ~2
        L, R = 0, i - 1  # linear scan
        while L < R:
            if nums[L] + nums[R] <= nums[i]:  # invalid(too small), move L
                L += 1
            else:  # all valid, try smaller, move R
                res += R - L
                R -= 1

    return res