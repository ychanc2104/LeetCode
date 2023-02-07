# https://leetcode.com/problems/shortest-way-to-form-string/
# https://leetcode.com/problems/shortest-way-to-form-string/solutions/399353/python-o-m-n-using-hash-table-space-o-m-with-notes/


import functools

# first thought, dfs, top-down dp, TC:O(NM), SC:O(M) M is size of source
def shortestWay(source: str, target: str) -> int:
    source_set = set(source)
    ns, nt = len(source), len(target)

    @functools.lru_cache(None)
    def helper(ps=0, pt=0):
        if pt == nt:
            return 0
        if target[pt] not in source_set:
            return -nt
        res = 0
        if source[ps] == target[pt]:
            if ps + 1 == ns:
                res += helper(0, pt + 1) + 1
            else:
                res += helper(ps + 1, pt + 1) + (1 if pt + 1 == nt else 0)
        else:
            if ps + 1 == ns:
                res += helper(0, pt) + 1
            else:
                res += helper(ps + 1, pt)
        return res

    res = helper(0, 0)
    return res if res > 0 else -1

# two pointers, TC:O(NM), SC:O(1)
def shortestWay2(source: str, target: str) -> int:
    source_set = set(source) # SC:O(1)
    ns, nt = len(source), len(target)
    # dp[i]: min number of sub at given target[:i]
    pt = ps = 0
    res = 0
    while pt < nt:
        if target[pt] not in source_set:
            return -1
        if target[pt] == source[ps]:
            ps += 1
            pt += 1
        else: # optimization: if not equal, directly jump to desired position
            ps += 1
        if ps == ns or pt == nt:
            ps = 0
            res += 1
    return res

# two pointers with cache, TC:O(N + M), SC:O(M) M is size of source
def shortestWay3(source: str, target: str) -> int:
    source_set = set(source)
    ns, nt = len(source), len(target)
    memo = {}  # ex: abcad,
    # For source = 'abba' the table looks like this:
    # {3: {'a': 4}, 2: {'a': 4, 'b': 3}, 1: {'a': 4, 'b': 2}, 0: {'a': 1, 'b': 2}}
    for i in range(ns - 1, -1, -1):
        char = source[i]
        memo[i] = {} if i + 1 not in memo else memo[i + 1].copy()
        memo[i][char] = i + 1 # jump to next

    # print(memo)
    ps = 0
    res = 1
    for pt in range(nt):
        if target[pt] not in source_set:
            return -1
        if ps == ns or target[pt] not in memo[ps]:  # if not in => must start a new subsequence
            ps = 0
            res += 1
        # optimization: directly jump to desired position
        ps = memo[ps][target[pt]]  # go to the next position of target[pt] in the source

    return res