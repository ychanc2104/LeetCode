# https://leetcode.com/problems/next-greater-element-ii/


# first thought, monotonic stack, TC:O(N), SC:O(N)
def nextGreaterElements(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [-1] * n
    stack = []
    for i in range(2 * n):
        while stack and nums[stack[-1]] < nums[i % n]:
            idx = stack.pop()
            if res[idx] != -1: continue
            res[idx] = nums[i % n]
        stack.append(i % n)
    return res