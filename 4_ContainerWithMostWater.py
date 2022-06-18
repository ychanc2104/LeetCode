# https://leetcode.com/problems/container-with-most-water/
# https://leetcode.com/problems/container-with-most-water/discuss/6100/Simple-and-clear-proofexplanation


def maxArea(height):
    n = len(height)
    V = min(height[0], height[n - 1]) * (n - 1)
    i, j = 0, 0
    while i != n - 1 - j:
        L = height[i]
        R = height[n - 1 - j]
        W = n - 1 - j - i
        if R > L:
            V_new = L * W
            i += 1
        else:
            V_new = R * W
            j += 1
        if V < V_new:
            V = V_new
    return V

# TC: O(n)
def maxArea2(height):
    L = 0
    R = len(height) - 1
    area = 0
    # from outside to inside
    while R > L:
        # record each area
        area = max(area, min(height[L], height[R]) * (R - L))
        if height[R] > height[L]:
            # find bigger height[L]
            L += 1
        else:
            # maintain L and shift R and try to reach bigger height[R]
            R -= 1
    return area

height = [1,8,6,2,5,4,8,3,7]
Area = maxArea(height)