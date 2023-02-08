# https://leetcode.com/problems/integer-break/description/
# https://leetcode.com/problems/integer-break/solutions/484055/rz-o-n-2-dp-solution-and-o-n-solution-based-on-math/
# https://leetcode.com/problems/integer-break/solutions/80689/a-simple-explanation-of-the-math-part-and-a-o-n-solution/


# first thought, top-down dp, TC:O(N^2) for N states, SC:O(N)
def integerBreak(n: int) -> int:
    # 3 = 2+1
    @functools.lru_cache(None)
    def helper(n):
        if n == 0:
            return 1
        res = 1
        for i in range(1, n):
            res = max(res, i * (n - i), i * helper(n - i))
        return res

    return helper(n)


# bottom-up dp, TC:O(N^2), SC:O(N)
def integerBreak2(n: int) -> int:
    # dp[3] = 2, dp[4] = 3, dp[5] = 6
    dp = [1] * (n+1)
    for i in range(2, n+1):
        for j in range(1, i):
            dp[i] = max(dp[i], (i - j) * j, j * dp[i-j])
    return dp[-1]


# math, TC:O(N), SC:O(1)
def integerBreak3(n: int) -> int:
    # math, use 3 or 4
    if n <= 2: return 1
    if n == 3: return 2
    res = 1
    while n > 4:
        res *= 3
        n -= 3
    return res * n # *3 or *4


# math, TC:O(logN), x**N => power's TC is logN, SC:O(1)
def integerBreak4(n: int) -> int:
    # f(4) = 4, f(5) = 6, f(6) = 9, f(7) = 12, f(8) = 18, f(9) = 27
    if n <= 2: return 1
    if n == 3: return 2
    if n % 3 == 0:
        return 3**(n//3)
    elif n % 3 == 1:
        return 3**(n//3 - 1) * 4
    else:
        return 3**(n//3) * 2