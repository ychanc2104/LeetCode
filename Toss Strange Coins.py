# https://leetcode.com/problems/toss-strange-coins/description/
# https://leetcode.com/problems/toss-strange-coins/solutions/418317/python3-top-down-dp-easy-with-picture/
# https://leetcode.com/problems/toss-strange-coins/solutions/408485/java-c-python-dp/


import functools

# top-down dp, TC:O(NM), SC:O(NM)
def probabilityOfHeads(prob: List[float], target: int) -> float:
    n = len(prob)

    @functools.lru_cache(None)
    def helper(i, target):
        if i == n:
            if target == 0:  # valid
                return 1
            return 0  # invalid
        if target == 0:  # no coin can be tossed
            return (1 - prob[i]) * helper(i + 1, target)
        return prob[i] * helper(i + 1, target - 1) + (1 - prob[i]) * helper(i + 1, target)

    return helper(0, target)

# bottom-up dp, TC:O(NM), SC:O(NM)
def probabilityOfHeads2(prob: List[float], target: int) -> float:
    n = len(prob)
    dp = [[0] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        dp[i][0] = (1 - prob[i - 1]) * dp[i - 1][0]  # choose i-th coin

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            dp[i][j] = prob[i - 1] * dp[i - 1][j - 1] + (1 - prob[i - 1]) * dp[i - 1][j]

    return dp[-1][-1]


# space-optimized bottom-up dp, TC:O(NM), SC:O(M)
def probabilityOfHeads2(prob: List[float], target: int) -> float:
    n = len(prob)
    dp = [0 for _ in range(target+1)]
    dp[0] = 1
    for i in range(1, n+1):
        dp_prev = dp.copy()
        for j in range(target+1):
            if j == 0:
                dp[j] = (1-prob[i-1]) * dp_prev[j]
            else:
                dp[j] = prob[i-1] * dp_prev[j-1] + (1-prob[i-1]) * dp_prev[j]

    return dp[-1]