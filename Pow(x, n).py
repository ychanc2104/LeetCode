# https://leetcode.com/problems/powx-n/
# https://leetcode.com/problems/powx-n/discuss/19560/Shortest-Python-Guaranteed


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

# iterative fast power, TC:O(logN), SC:O(1)
def myPow2(x: float, n: int) -> float:
    if n < 0:
        x = 1 / x
        n = -n
    # 2^10, (n,x,res)=>(10,2^2,1),(5,2^4,2^2),(2,2^8,2^2),(1,2^16,2^10), (0,end)
    res = 1
    while n > 0:
        if n & 1:
            res *= x
        x *= x
        n = n // 2
    return res

# recursive fast power, TC:O(logN), SC:O(logN)
def myPow3(x: float, n: int) -> float:
    if n < 0:
        return myPow3(1 / x, -n)
    elif n == 0:
        return 1
    elif n & 1:
        return x * myPow3(x * x, n >> 1)
    else:
        return myPow3(x * x, n >> 1)