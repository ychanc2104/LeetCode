# https://leetcode.com/problems/coin-change-ii/description/
# https://leetcode.com/problems/coin-change-ii/solutions/99209/python-recursive-solution-slow/



import functools


# first thought, dp, TC:O(NM + NlogN), SC:O(NM) NM states
def change(amount: int, coins: List[int]) -> int:
    coins.sort()

    @functools.lru_cache(None)
    def helper(amount, prev_coin=-1):  # make path increasing
        if amount == 0:
            return 1  # one path found
        res = 0
        for c in coins:
            if c < prev_coin or amount - c < 0:
                continue
            res += helper(amount - c, c)
        return res

    return helper(amount)

# bottom-up dp, TC:O(NM), SC:O(M) M is amount
def change2(amount: int, coins: List[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1
    for c in coins:  # fill in every coin, get combination
        for a in range(c, amount + 1):
            dp[a] += dp[a - c]  # from all other source adding c, like x,y,z,...+ c
    # print(dp)
    return dp[amount]


# top-down dp, TC:O(NM), SC:O(M) M is amount
def change3(amount: int, coins: List[int]) -> int:

    @functools.lru_cache(None)
    def helper(amount, i):  # make path increasing
        if i == len(coins) or amount < 0:
            return 0
        if amount == 0:
            return 1
        c = coins[i]
        return helper(amount - c, i) + helper(amount, i+1) # use first coin and next coin

    return helper(amount, 0)