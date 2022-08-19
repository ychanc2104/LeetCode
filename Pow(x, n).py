# https://leetcode.com/problems/powx-n/

# TC:O(N), SC:O(1)
def myPow(x: float, n: int) -> float:
    if n == 0: return 1
    if n < 0:
        x = 1 / x
        n = -n
    res = 1
    while n > 0:
        n -= 1
        res *= x
    return res

# fast power, TC:O(logN), SC:O(1)
def myPow2(x: float, n: int) -> float:
    if n==0: return 1
    if n < 0:
        x = 1/x
        n = -n
    # x^8, (n, res)=>(8,x^2),(4,x^$),(2,x^8),(1,end)
    res = x
    while n > 1:
        if n % 2 == 1:
            res *= x
        res = res*res
        n = n//2
    return res