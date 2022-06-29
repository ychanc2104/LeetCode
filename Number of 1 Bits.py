# https://leetcode.com/problems/number-of-1-bits/


# first thought
def hammingWeight(n: int) -> int:
    res = 0
    ## end with n==0
    while n > 0:
        # count odd num
        if n % 2 == 1:
            res += 1
        n = n >> 1

    return res

def hammingWeight2(n: int) -> int:
    ans = 0
    while n:
        # n&(n-1) will remove the rightmost
        n = n&(n-1)
        ans += 1
    return ans


def hammingWeight3(n: int) -> int:
    count = 0
    while n != 0:
        count += n & 1
        n = n >> 1
    return count
