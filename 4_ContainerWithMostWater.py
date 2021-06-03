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

height = [1,8,6,2,5,4,8,3,7]
Area = maxArea(height)