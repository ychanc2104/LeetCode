# https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/
# https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/solutions/623732/java-c-python-dp-prefixsum-in-matrix-clean-code/


import functools


# top-down dp, prefix sum, TC:O(NMk(N+M)), SC:O(NMk)
def ways(pizza: List[str], k: int) -> int:
    n, m = len(pizza), len(pizza[0])
    # to prevent duplicates counting, actually is suffix sum
    prefix = [[0] * m for _ in range(n)]  # prefix[i][j]: sum from [i,j] to [n-1,m-1]
    for i in range(n - 1, -1, -1):
        s_col = 0
        for j in range(m - 1, -1, -1):
            s_col += (pizza[i][j] == "A")
            prefix[i][j] = (prefix[i + 1][j] if i < n - 1 else 0) + s_col

    # states = knm
    @functools.lru_cache(None)
    def helper(k, r, c):  # ways from [r, c] to [n-1, m-1] grid
        if prefix[r][c] == 0:
            return 0
        if k == 1:
            return 1
        res = 0
        # cut horizontal
        for rc in range(r + 1, n):
            if (prefix[r][c] - prefix[rc][c]) > 0:  # upper part
                # continue
                res += helper(k - 1, rc, c)  # lower part

        for cc in range(c + 1, m):
            if (prefix[r][c] - prefix[r][cc]) > 0:  # left part
                # continue
                res += helper(k - 1, r, cc)  # right
        return res % (10 ** 9 + 7)

    return helper(k, 0, 0)