# https://leetcode.com/problems/sliding-window-maximum/
# https://leetcode.com/problems/sliding-window-maximum/discuss/871317/Clear-thinking-process-with-PICTURE-brute-force-to-mono-deque-pythonjavajavascript

import collections

# deque, TC:O(N), SC:O(k) for deque, output take O(N-k)
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    # return size => n-k+1
    # initiate queue
    queue = collections.deque([])  # store indices, in decreasing order
    res = []
    for i in range(len(nums)):
        while queue and nums[i] > nums[queue[-1]]:
            queue.pop()
        queue.append(i)
        # remove node exceeded window, max size of queue if k
        if queue[0] <= i - k:
            queue.popleft()
            # store result start from i==k-1
        if i >= k - 1:
            res.append(nums[queue[0]])
    return res

# dp, TC:O(N), SC:O(N)
def maxSlidingWindow2(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    if n * k == 0:
        return []
    if k == 1:
        return nums

    left = [0] * n
    left[0] = nums[0]
    right = [0] * n
    right[n - 1] = nums[n - 1]
    for i in range(1, n):
        # from left to right
        if i % k == 0:
            # block start
            left[i] = nums[i]
        else:
            left[i] = max(left[i - 1], nums[i])
        # from right to left
        j = n - i - 1
        if (j + 1) % k == 0:
            # block end
            right[j] = nums[j]
        else:
            right[j] = max(right[j + 1], nums[j])

    output = []
    for i in range(n - k + 1):
        output.append(max(left[i + k - 1], right[i]))

    return output