# https://leetcode.com/problems/factorial-trailing-zeroes/description/


# first thought, compute 5's factor, TC:O(N), SC:O(1)
def trailingZeroes(n: int) -> int:
    # 1,2,3,4,5,6,7,8,9,10
    # 2,5,  counter of 5
    res = 0
    for i in range(1, n + 1):

        while i % 5 == 0: # TC:O(logN) but amortized O(1)
            res += 1
            i //= 5
    return res


# compute 5's factor, TC:O(logN), SC:O(1)
def trailingZeroes2(n: int) -> int:
    # 1,2,3,4,5,6,7,8,9,10
    # 2,5,  counter of 5
    res = 0
    while n >= 5:
        n //= 5
        res += n // 5
    return res