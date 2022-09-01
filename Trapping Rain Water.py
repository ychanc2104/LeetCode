# https://leetcode.com/problems/trapping-rain-water/


# two pointers, TC:O(N), SC:O(1)
def trap(height) -> int:
    res = 0
    L, R = 0, len(height) - 1
    maxL, maxR = height[L], height[R]
    # two pointers, TC:O(N), SC:O(1)
    while L < R:
        if height[L] < height[R]:
            if height[L] > maxL:
                maxL = height[L]
            else:
                res += maxL - height[L]
            L += 1
        else:
            if height[R] > maxR:
                maxR = height[R]
            else:
                res += maxR - height[R]
            R -= 1
    return res


# dp, TC:O(N), SC:O(N)
def trap2(height) -> int:
    res = 0
    n = len(height)
    dp_left = [0] * n
    tempMax = 0
    for i in range(n):
        if height[i] > tempMax:
            tempMax = height[i]
        dp_left[i] = (tempMax)
    dp_right = [0] * n
    tempMax = 0
    for j in range(n-1,-1,-1):
        if height[j] > tempMax:
            tempMax = height[j]
        dp_right[j] = tempMax
    # merge two dp table
    for k in range(n):
        res += min(dp_left[k], dp_right[k]) - height[k]
    return res


