# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/submissions/845089931/

# first thought, TC:O(N), SC:O(1)
def numPairsDivisibleBy60(time: List[int]) -> int:
    memo = {}
    res = 0
    for t in time:
        t = t % 60
        target = (60 - t) % 60
        if t in memo:
            res += memo[t]
        memo[target] = memo.get(target, 0) + 1
    return res