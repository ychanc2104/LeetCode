# https://leetcode.com/problems/minimum-impossible-or/description/
# https://leetcode.com/problems/minimum-impossible-or/solutions/3201897/java-c-python-pow-of-2/
# https://leetcode.com/problems/minimum-impossible-or/solutions/3201924/explained-two-solutions-with-without-extra-space-very-simple-easy-to-understand/


# TC:O(N), SC:O(N)
def minImpossibleOR(nums: List[int]) -> int:
    nums_set = set(nums)
    for i in range(32):
        if 2 ** i not in nums_set:
            return 2 ** i

# TC:O(N), SC:O(1)
def minImpossibleOR2(nums: List[int]) -> int:
    check = 0
    for num in nums:
        if num & (num - 1) == 0:  # is power of 2
            check |= num  # fill in power of 2

    return ~check & (check + 1)