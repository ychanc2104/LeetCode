# https://leetcode.com/problems/largest-rectangle-in-histogram/
# https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/995249/Python-increasing-stack-explained


# monotonic increasing stack, TC:O(n), SC:O(n)
def largestRectangleArea(heights) -> int:
    stack, ans = [], 0
    for i, h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] >= h:  # non-increasing case
            H = heights[stack.pop()]
            W = i if not stack else i - stack[-1] - 1  # stack[-1] is left bound(not including)
            ans = max(ans, H * W)
        stack.append(i)
    return ans