# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/

# first thought, prefix sum, TC:O(N), SC:O(N)
def subarraysDivByK(nums: List[int], k: int) -> int:
    memo = {0: 1}
    prefix_sum = 0
    res = 0
    for num in nums:
        prefix_sum += num
        target = (prefix_sum - k) % k
        if target in memo:
            res += memo[target]
        memo[prefix_sum % k] = memo.get(prefix_sum % k, 0) + 1
    return res

# prefix sum, TC:O(N), SC:O(N)
def subarraysDivByK2(nums: List[int], k: int) -> int:
    m = {0: 1}
    s = 0
    res = 0
    for num in nums:
        s = (s + num) % k
        res += m.get(s, 0)
        m[s] = m.get(s, 0) + 1

    return res