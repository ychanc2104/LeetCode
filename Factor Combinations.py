# https://leetcode.com/problems/factor-combinations/


import functools, collections

# first thought, top-down dp, TC:O(n^1.5), SC:O(n^0.5 + n)
def getFactors(n: int) -> List[List[int]]:
    @functools.lru_cache(None)
    def helper(n):
        if n == 1:
            return []
        res = [[n]]
        for factor in range(2, int(n ** 0.5) + 1):
            if n % factor == 0:
                q = n // factor
                for sub in helper(q):
                    if sub and factor <= sub[0]:
                        res.append([factor] + sub)
        return res

    return helper(n)[1:]


# first thought, top-down dp, TC:O(n^1.5), SC:O(n^0.5 + n)
def getFactors2(n: int) -> List[List[int]]:
    @functools.lru_cache(None)
    def helper(n):
        if n == 1:
            return []
        res = []
        for factor in range(2, int(n ** 0.5) + 1):
            if n % factor == 0:
                q = n // factor
                for sub in helper(q):
                    if sub and factor <= sub[0]: # make res increasing
                        res.append([factor] + sub)
        res.append([n])
        return res

    return helper(n)[:-1]


# top-down dp, TC:O(n^1.5), SC:O(n^0.5 + n)
def getFactors3(n: int) -> List[List[int]]:
    memo = {}
    def helper(n, start=2):
        if n == 1:
            return []
        if (n, start) in memo:
            return memo[(n, start)]
        res = []
        for factor in range(start, int(n ** 0.5) + 1): # make res increasing
            if n % factor == 0:
                q = n // factor
                for sub in helper(q, factor):
                    res.append([factor] + sub)
        res.append([n])
        memo[(n, start)] = res
        return res

    return helper(n)[:-1]

# bottom-up dp, TC:O(n^1.5), SC:O(n^0.5 + n)
def getFactors4(n: int) -> List[List[int]]:
    dp = collections.defaultdict(list)
    for i in range(3, n+1):
        for f in range(2, int(i**0.5) + 1):
            if i % f == 0:
                q = i//f
                dp[i].append([f, q])
                for sub in dp[q]:
                    if sub and f <= sub[0]:
                        dp[i].append([f] + sub)

    return dp[n]


# backtracking, TC:O(n^1.5), SC:O(logn), logn for path length and recursion depth
def getFactors5(n: int) -> List[List[int]]:
    res = []
    path = [n] # decompose n first
    def backtrack(start):
        if path:
            res.append(path[:])

        prev_num = path.pop()
        for f in range(start, int(prev_num**0.5) + 1): # make path increasing
            if prev_num % f == 0:
                path.append(f)
                path.append(prev_num // f)
                backtrack(f)
                path.pop()
                path.pop()
        path.append(prev_num) # restart, decompose prev_num
    backtrack(2)
    return res[1:]