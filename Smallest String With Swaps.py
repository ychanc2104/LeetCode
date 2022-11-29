# https://leetcode.com/problems/smallest-string-with-swaps/?envType=study-plan&id=graph-ii
# https://leetcode.com/problems/smallest-string-with-swaps/solutions/1985185/python3-union-find-explained/

import collections

# union find + hash, TC:O((N+M)*alpha(N)+NlogN) N is len(s) and M is len(pairs), SC:O(N)
def smallestStringWithSwaps(s: str, pairs: list[list[int]]) -> str:
    # union pairs, traverse all connect components
    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px < py:
            parents[py] = px
        else:
            parents[px] = py

    parents = [i for i in range(len(s))] # SC:O(N)
    for x, y in pairs: # TC:O(M*alpha(N))
        union(x, y)
    # group
    group = collections.defaultdict(lambda: [[], []])
    for pos, l in enumerate(s): # TC:O(N*alpha(N)), SC:O(N)
        px = find(pos)
        group[px][0].append(l)  # store alphabet
        group[px][1].append(pos)  # its pos to be replaced
    res = ['' for _ in range(len(s))]
    for i in range(len(s)): # TC:O(N)
        if res[i]: continue
        px = find(i)
        nodes = sorted(group[px][0]) # TC:O(NlogN)
        idx = sorted(group[px][1])
        for i, n in zip(idx, nodes):
            res[i] = n

    return ''.join(res)

# union find + hash, TC:O((N+M)*alpha(N)+NlogN) N is len(s) and M is len(pairs), SC:O(N)
def smallestStringWithSwaps2(s: str, pairs: list[list[int]]) -> str:

    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px < py:
            parents[py] = px
        else:
            parents[px] = py

    parents = [i for i in range(len(s))]
    for a, b in pairs:
        union(a, b)
    group = {}
    for x, l in enumerate(s):
        px = find(x)
        if px not in group:
            group[px] = [[x], [l]]
        else:
            group[px][0].append(x)
            group[px][1].append(l)
    res = ['' for _ in s]
    for idx, letters in group.values():
        for i, l in zip(sorted(idx), sorted(letters)):
            res[i] = l
    return ''.join(res)