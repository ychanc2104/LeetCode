# https://leetcode.com/problems/best-sightseeing-pair/description/

# dp, TC:O(N), SC:O(1)
def maxScoreSightseeingPair(values: List[int]) -> int:
    L = 0
    R = 1
    res = values[L] + values[R] + L - R
    for R in range(2, len(values)):
        if values[L] + L < values[R - 1] + R - 1:
            # move L
            L = R - 1
        if L < R:
            res = max(res, values[L] + values[R] + L - R)
    return res

# dp, TC:O(N), SC:O(1)
def maxScoreSightseeingPair2(values: List[int]) -> int:
    # store best i and iterate all j
    iBest = 0
    res = float("-inf")
    for j in range(1, len(values)):
        res = max(res, values[iBest] + iBest + values[j] - j)
        if values[iBest] + iBest < values[j] + j:
            # move L
            iBest = j
    return res

# dp, TC:O(N), SC:O(1)
def maxScoreSightseeingPair3(values: List[int]) -> int:
    # store best i and iterate all j
    first = values[0]
    res = float("-inf")
    for j in range(1, len(values)):
        res = max(res, first + values[j] - j)
        first = max(first, values[j] + j)
    return res