# https://leetcode.com/problems/squares-of-a-sorted-array/
# https://leetcode.com/problems/squares-of-a-sorted-array/discuss/310865/Python%3A-A-comparison-of-lots-of-approaches!-Sorting-two-pointers-deque-iterator-generator
# https://leetcode.com/problems/squares-of-a-sorted-array/discuss/233054/Python-sorted()-solution-is-O(N)-not-O(NlogN)


# first thought, TC:O(n), SC:O(n)
def sortedSquares(nums):
    stack = []  # for negative numbers
    res = []
    for num in nums:
        # first prev is largest negative
        # -4,-1,0,3,10
        if num < 0:
            stack.append(num)
        else:
            if not stack:
                res.append(num ** 2)
            else:
                if stack[-1] ** 2 > num ** 2:
                    # use num
                    res.append(num ** 2)
                else:
                    # use stack and num
                    while stack and stack[-1] ** 2 <= num ** 2:
                        res.append(stack.pop() ** 2)
                    # exit when num**2 is smaller or stack is empty
                    res.append(num ** 2)
    while stack:
        res.append(stack.pop() ** 2)
    return res

# first thought, cleaner, TC:O(n), SC:O(n)
def sortedSquares2(nums):
    stack = []  # for negative numbers
    res = []
    for num in nums:
        # -4,-1,0,3,10
        if num < 0:
            stack.append(num)
        else:
            if stack:
                # use stack and num
                while stack and stack[-1] ** 2 <= num ** 2:
                    res.append(stack.pop() ** 2)
                # exit when num**2 is smaller or stack is empty
            res.append(num ** 2)
    while stack:
        res.append(stack.pop() ** 2)
    return res

# two pointers, cleaner, TC:O(n), SC:O(1)
def sortedSquares3(nums):
    # append res from the biggest to the smallest
    # -4,-1,0,3,10
    n = len(nums)
    L, R = 0, n-1
    res = [0] * n
    for i in range(n):
        if nums[L]**2 > nums[R]**2:
            # update bigger one
            res[n-1-i] = nums[L]**2
            L += 1
        else:
            res[n-1-i] = nums[R]**2
            R -= 1
    return res

