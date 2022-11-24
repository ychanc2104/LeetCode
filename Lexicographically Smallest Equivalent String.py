# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description/?envType=study-plan&id=graph-ii


# first thought, union find, TC:O(N+M), SC:O(1)
def smallestEquivalentString(s1: str, s2: str, baseStr: str) -> str:
    parents = [i for i in range(26)]
    memo = {i: chr(ord('a') + i) for i in range(26)}

    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px <= py:
            parents[py] = px
        else:
            parents[px] = py

    for c1, c2 in zip(s1, s2): # TC:O(N)
        x, y = ord(c1) - ord('a'), ord(c2) - ord('a')
        union(x, y)
    res = []
    for char in baseStr: # TC:O(M)
        x = ord(char) - ord('a')
        res.append(memo[find(x)])
    return ''.join(res)