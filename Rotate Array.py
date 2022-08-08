# https://leetcode.com/problems/rotate-array/


# connect as a circle ,TC:O(N), SC:O(N)
def rotate(nums, k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # 1,2,3,4,5,6,7 k=3
    # 5,6,7,1,2,3,4 (0,1,2,3,4,5,6)=>(4,5,6,0,1,2,3)
    # 1,2,3,4 k=2
    # 3,4,1,2 (0,1,2,3) => (2,3,0,1)
    n = len(nums)
    res = [0] * len(nums)
    for i in range(len(nums)):
        # imagine to connect as a circle(length n), starting index shift k
        res[i] = nums[(n - k + i) % n]
        ## or
        # res[(i + k) % n] = nums[i]
    nums[:] = res

# connect as a circle ,TC:O(N), SC:O(1)
def rotate2(nums, k: int) -> None:
    n = len(nums)
    count = 0
    start = 0
    while count < n:
        # store previous num to be replaced
        current, prev = start, nums[start]
        # prevent cyclic looping
        while True:
            index = (current + k) % n
            nums[index], prev = prev, nums[index]
            current = index
            count += 1
            if start == current:
                break
        start += 1

# reverse ,TC:O(N), SC:O(1)
def rotate3(nums, k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # Original List                   : 1 2 3 4 5 6 7
    # After reversing all numbers     : 7 6 5 4 3 2 1
    # After reversing first k numbers : 5 6 7 4 3 2 1
    # After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result
    def reverse(i, j):
        # reverse nums from i to j [i,j]
        # two pointers
        L, R = i, j
        while L < R:
            nums[L], nums[R] = nums[R], nums[L]
            L += 1
            R -= 1

    n = len(nums)
    k = k % n
    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
