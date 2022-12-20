# https://leetcode.com/problems/next-greater-element-iii/

# first thought, TC:O(logN), SC:O(logN)
def nextGreaterElement(n: int) -> int:
    # next permutation
    nums = []
    n_temp = n
    while n:
        nums.append(n % 10)
        n //= 10
    nums.reverse()
    # print(nums)
    # 2,3,5,1,6 => 2,3,5,6,1 => 2,3,6,5,1 => 2,5,1,3,6
    # 2,5,5,3,1 => 3,1,2,5,5
    # 5,2,2,3,1 => 5,2,3,1,2
    # from bottom
    # 1. find first non-increasing element(strickly)
    l = len(nums)
    pivot = 0
    for i in range(l - 2, -1, -1):
        if nums[i + 1] > nums[i]:
            pivot = i
            break
    # 2. find first number(idx) is greater than nums[pivot]
    idx = l - 1
    for i in range(l - 1, -1, -1):
        if nums[i] > nums[pivot]:
            idx = i
            break
    # 3. swap 1,2
    nums[pivot], nums[idx] = nums[idx], nums[pivot]
    # 4. reverse nums[pivot+1:]
    nums[pivot + 1:] = nums[pivot + 1:][::-1]
    # 5. recover to int
    max_int = 2 ** 31 - 1
    res = 0
    nums.reverse()
    while nums:
        digit = nums.pop()
        if res > max_int // 10:
            return -1
        res *= 10
        if res > max_int - digit:
            return -1
        res += digit
    return res if res > n_temp else -1