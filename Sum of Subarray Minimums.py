# https://leetcode.com/problems/sum-of-subarray-minimums/

# dp + monotonic stack, TC:O(N), SC:O(N)
def sumSubarrayMins(arr: List[int]) -> int:
    # dp[i]: res of ending with arr[i]
    # return sum(dp)
    # if stack => dp[stack[-1]] + (i - stack[-1]) * arr[i]
    # if not stack => (i-j) * arr[i]
    stack = []  # store index with increasing value
    dp = [0] * len(arr)
    for i in range(len(arr)):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        else:
            if not stack:  # arr[i] is current min
                dp[i] = (i + 1) * arr[i]
            else:
                prev = stack[-1]
                dp[i] = dp[prev] + (i - prev) * arr[i]
            stack.append(i)  # add new min
    return sum(dp) % (10 ** 9 + 7)