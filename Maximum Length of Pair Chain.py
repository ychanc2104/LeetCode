# https://leetcode.com/problems/maximum-length-of-pair-chain/description/
# https://leetcode.com/problems/maximum-length-of-pair-chain/solutions/225801/proof-of-the-greedy-solution/


# first thought, TC:O(N^2), SC:O(N)
def findLongestChain(pairs: List[List[int]]) -> int:
    # dp[i]: longest chain end with index i
    n = len(pairs)
    pairs.sort()
    dp = [1] * n
    for i in range(n):
        c, d = pairs[i]
        for j in range(i):
            a, b = pairs[j]
            if c > b:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


# greedy, TC:O(NlogN), SC:O(N) for sort
def findLongestChain2(pairs: List[List[int]]) -> int:
    n = len(pairs)
    pairs.sort()
    end = pairs[0][1]
    res = 1
    for i in range(1, n):
        c, d = pairs[i]
        if c > end:
            res += 1
            end = d
        end = min(end, d) # use smaller end
    return res


# greedy, TC:O(NlogN), SC:O(N) for sort
def findLongestChain3(pairs: List[List[int]]) -> int:
    n = len(pairs)
    pairs.sort(key=lambda x: x[1])
    end = pairs[0][1]
    res = 1
    for i in range(1, n):
        c, d = pairs[i]
        if c > end:
            res += 1
            end = d # must be smaller end
    return res