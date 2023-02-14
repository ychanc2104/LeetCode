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


# use monotonic stack, TC:O(N), SC:O(N)
def trap3(height) -> int:
    # stack to store each index
    stack = []
    res = 0
    n = len(height)
    for i in range(n):
        # find the height is greater, bounded water
        while stack and height[i] > height[stack[-1]]:
            # bounded, calculate area of each bar
            i_prev = stack.pop()
            if not stack:
                break
            # calculate horizontal area (rectangle)
            h = min(height[i], height[stack[-1]]) - height[i_prev]
            width = i - stack[-1] - 1
            res += h * width
        stack.append(i)
    return res

# use monotonic stack, TC:O(N), SC:O(N)
def trap4(height) -> int:
    # stack, store idx if height
    stack = []
    res = 0
    for i in range(len(height)):
        h = height[i]
        while stack and h > height[stack[-1]]:
            idx = stack.pop()
            if stack:
                wall_idx = stack[-1]
                res += (i - wall_idx - 1) * (min(h, height[wall_idx]) - height[idx])
        stack.append(i)

    return res