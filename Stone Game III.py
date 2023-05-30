# https://leetcode.com/problems/stone-game-iii/description/

import functools

# first thought top-down dp, slow, TC:O(N), SC:O(N)
def stoneGameIII(stoneValue: List[int]) -> str:
    # find max of alice can get
    @functools.lru_cache(None)
    def helper(i, role=1):
        if i >= len(stoneValue):
            return 0

        res = float("-inf") if role == 1 else float("inf")
        s = 0

        for j in range(3):
            if i + j >= len(stoneValue): continue
            s += stoneValue[i + j]
            # print(role, i, s, res)
            if role == 1:  # alice
                res = max(res, helper(i + 1 + j, -1) + s)
            else:  # bob
                res = min(res, helper(i + 1 + j, 1))
        return res

    total = sum(stoneValue)
    alice = helper(0, 1)
    # print(alice, total)
    if alice * 2 > total:
        return "Alice"
    elif alice * 2 < total:
        return "Bob"
    return "Tie"

# first thought top-down dp, faster, TC:O(N), SC:O(N)
def stoneGameIII2(stoneValue: List[int]) -> str:
    # find max of alice can get
    n = len(stoneValue)

    @functools.lru_cache(None)
    def helper(i):
        if i >= n:
            return 0

        s = stoneValue[i]
        res = s - helper(i + 1)
        if i + 1 < n:
            s += stoneValue[i + 1]
            res = max(res, s - helper(i + 2))

        if i + 2 < n:
            s += stoneValue[i + 2]
            res = max(res, s - helper(i + 3))
        return res

    diff = helper(0)
    # print(alice, total)
    if diff > 0:
        return "Alice"
    elif diff < 0:
        return "Bob"
    return "Tie"