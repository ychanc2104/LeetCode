def missingNumber(nums):
    # 1,2,3 =>6 and 6
    # 0,1,2 =>3 and 6
    n = len(nums)
    return int(n * (n + 1) / 2 - sum(nums))


# bit manipulation, TC:O(n), SC:O(1)
def missingNumber2(nums):
    # bit, 0^1^2^1^2^3 = 3, 0^2^3^1^2^3 = 1, 0^1^2^1^2^3 = 3
    res = 0 # 0 no effect for XOR
    for i,num in enumerate(nums,1):
        res ^= num^i
    return res