# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

import functools, collections

# top down dp, TC:O(NMk) k is len(words), N is len(words[0]), M is len(target), SC:O(NM)
def numWays(words: List[str], target: str) -> int:
    mod = 10 ** 9 + 7

    @functools.lru_cache(None)
    def helper(k, idx):
        # count all path
        # idx is index of target
        if idx == len(target):
            return 1
        if k == len(words[0]):
            return 0

        # from kth index
        res = helper(k + 1, idx)
        for j in range(len(words)):
            if words[j][k] == target[idx]:
                res += helper(k + 1, idx + 1)  # use
        return res % (mod)

    return helper(0, 0)

# top down dp, TC:O(NM), SC:O(NM)
def numWays2(words: List[str], target: str) -> int:
    memo = [collections.Counter() for _ in range(len(words[0]))]

    for i in range(len(words[0])):
        for j in range(len(words)):
            memo[i][words[j][i]] += 1

    mod = 10 ** 9 + 7

    @functools.lru_cache(None)
    def helper(k, idx):
        # count all path
        # idx is index of target
        if idx == len(target):
            return 1
        if k == len(words[0]):
            return 0

        # from kth index
        res = helper(k + 1, idx)  # skip this
        # speed up, to get how many chars at pos k
        res += helper(k + 1, idx + 1) * memo[k][target[idx]]  # use
        return res % (mod)

    return helper(0, 0)