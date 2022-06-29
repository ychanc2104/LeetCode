# https://leetcode.com/problems/palindrome-number/



# first thought, without using str(), TC:O(log10 n), SC:O(log10 n)
def isPalindrome(x: int) -> bool:
    if x < 0: return False
    nums = []
    while x:
        nums.append(x % 10)
        x //= 10
    n = len(nums)
    for i in range(n // 2):
        if nums[i] != nums[n - 1 - i]:
            return False
    return True


# TC:O(log10 n), SC:O(1)
def isPalindrome(x: int) -> bool:
    # all negative, xxxx0(not 0)
    if x < 0 or (x%10==0 and x!=0): return False
    x_rev = 0
    while x>x_rev:
        x_rev = x_rev*10 + x%10
        x = x//10
    return (x==x_rev) or (x==x_rev//10)