# https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=study-plan&id=binary-search-ii


# first thought, two pointers, TC:O(N), SC:O(1)
def minSubArrayLen(target: int, nums: List[int]) -> int:
    L, R = 0, 0
    tempSum = nums[L]
    res = float("inf")
    while L < len(nums):
        if tempSum >= target or R == len(nums) - 1:
            if tempSum >= target:  # update res
                res = min(res, R - L + 1)
            tempSum -= nums[L]
            L += 1
        else:
            R += 1
            tempSum += nums[R]
    return res if res != float("inf") else 0

# clean two pointers, TC:O(N), SC:O(1)
def minSubArrayLen2(target: int, nums: List[int]) -> int:
    L = 0
    tempSum = 0
    res = float("inf")
    for R in range(len(nums)):
        tempSum += nums[R]
        while tempSum >= target:  # update and move L
            res = min(res, R - L + 1)
            tempSum -= nums[L]
            L += 1

    return res if res != float("inf") else 0


# prefix sum + binary search, TC:O(NlogN), TC:O(N)
def minSubArrayLen(target: int, nums: List[int]) -> int:
    preSum = []
    tempSum = 0
    for num in nums:
        tempSum += num
        preSum.append(tempSum)
    # find all subarray
    res = float("inf")
    for i in range(len(nums)):
        L, R = i, len(nums)-1
        tempSum = preSum[i]
        # binary search(left most)
        while L <= R:
            mid = (L + R)//2
            t = preSum[mid] - tempSum + nums[i]
            if t >= target: # move R
                R = mid - 1
            else:
                L = mid + 1
        res = min(res, L - i + 1) if L < len(nums) else res
    return res if res != float("inf") else 0