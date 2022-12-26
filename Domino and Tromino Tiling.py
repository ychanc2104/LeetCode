# https://leetcode.com/problems/domino-and-tromino-tiling/description/

# top-down
def numTilings(n: int) -> int:
    # dp_d[i] = dp_d[i-1] + dp_d[i-2] + dp_t[i-2] * 2, number of ways fully covered to cover width i
    # dp_t[i] = dp_t[i-1] + dp_d[i-2], number of ways partial overlapped to cover width i
    mod = 10 ** 9 + 7
    memo_d = {0: 1, 1: 1, 2: 2}

    def dp_d(n):
        if n in memo_d:
            return memo_d[n]
        memo_d[n] = (dp_d(n - 1) + dp_d(n - 2) + dp_t(n - 1) * 2) % mod
        return memo_d[n]

    memo_t = {0: 0, 1: 0, 2: 1}

    def dp_t(n):
        if n in memo_t:
            return memo_t[n]
        memo_t[n] = (dp_t(n - 1) + dp_d(n - 2)) % mod
        return memo_t[n]

    return dp_d(n)