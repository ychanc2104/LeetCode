# https://leetcode.com/problems/single-number/
# https://leetcode.com/problems/single-number/discuss/1771771/Think-it-through-oror-Time%3A-O(n)-Space%3A-O(1)-oror-Python-Explained


# first thought, TC:O(n), SC:O(n)
def singleNumber(nums) -> int:
    memo = {}
    while nums:
        num = nums.pop()
        if num not in memo:
            memo[num] = 1
        else:
            memo.pop(num)
    return list(memo.keys())[0]

# use XOR, TC:O(n), SC:O(1)
# x^0 = x, x^x = 0, x^y^x = (x^x)^y = 0^y = y
def singleNumber(nums) -> int:
    res = 0
    for num in nums:
        res ^= num
    return res