# https://leetcode.com/problems/2-keys-keyboard/
# https://leetcode.com/problems/2-keys-keyboard/solutions/105899/java-dp-solution/
# https://leetcode.com/problems/2-keys-keyboard/solutions/105897/loop-best-case-log-n-no-dp-no-extra-space-no-recursion-with-explanation/


import functools

# first thought, top-down dp, TC:O(N^2), SC:O(N^2), 1+2+3+..+N = N^2 states
def minSteps(n: int) -> int:
    @functools.lru_cache(None)
    def helper(count=1, copy=0):
        if count == n:
            return 0
        if count > n:
            return float('inf')

        opt1 = float('inf')
        # copy
        if count != copy:
            opt1 = helper(count, count) + 1
        opt2 = float('inf')
        if copy:
            # paste
            opt2 = helper(count + copy, copy) + 1

        return min(opt1, opt2)

    # (1,0)(3) => (1,1)(2) => (2,1)(1) => (2,2)(-inf) and (3,1)(0) => (4,2)
    return helper()


# bottom-up dp, TC:O(N^2), SC:O(N^2)
def minSteps2(n: int) -> int:
    if n == 1:
        return 0
    dp = [[float('inf')] * (n + 1) for _ in
          range(n + 1)]  # dp[n][count]: min opt at given length count in clipboard and length n
    dp[1][1] = 1

    for i in range(2, n + 1):
        m = float('inf')
        for j in range(1, i + 1):
            if i == j:
                dp[i][j] = m + 1
            if i == j or dp[i - j][j] == float('inf'): continue

            dp[i][j] = dp[i - j][j] + 1
            m = min(m, dp[i][j])
    # print(dp)
    return m


# space-optimized bottom-up dp, TC:O(N^2), SC:O(N)
def minSteps3(n: int) -> int:
    dp = [0] * (n + 1) # dp[n][count]: min opt at given length count in clipboard and length n
    for i in range(2, n+1):
        dp[i] = i # max i times
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i//j)
    # print(dp)
    return dp[-1]



# math, [CPP][CP] C always come after multiple P, TC:O(N^0.5), SC:O(1)
def minSteps4(n: int) -> int:
    # d steps to get n/d
    ans = 0
    d = 2
    while n > 1:
        while n % d == 0: # d is common factor of n
            ans += d
            n /= d # factorization
        d += 1 # copy
    return ans