# https://leetcode.com/problems/unique-binary-search-trees/description/


# dp, TC:O(n^2), SC:O(n)
def numTrees(n: int) -> int:
    # 1,2,3,4,5,6=> Left, x, Right
    # f(n) = summation(f(i)*f(n-i-1))
    f = [0] * (n + 1)
    f[0], f[1] = 1, 1
    for i in range(2, n + 1):
        for j in range(i):
            f[i] += f[j] * f[i - 1 - j]
    return f[-1]

# math, TC:O(n), SC:O(1), Catalan number:Cn+1 = 2*(2n+1)/(n+2) * Cn
def numTrees2(n: int) -> int:
    f = 1
    for i in range(1,n):
        f = 2*(2*i+1)/(i+2) * f
    return int(f)