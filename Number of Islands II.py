# https://leetcode.com/problems/number-of-islands-ii/
# https://leetcode.com/problems/number-of-islands-ii/solutions/75468/compact-python/

import collections

# union find, TC:O(N*alpha(N)), SC:O(N) N is length of positions(prevent double counting)
def numIslands2(m: int, n: int, positions: List[List[int]]) -> List[int]:
    parents = [i for i in range(len(positions))]

    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px == py:  # already same group, do nothing
            return 0
        parents[px] = py
        return 1

    table = collections.defaultdict(int)
    for i, pos in enumerate(positions):
        table[tuple(pos)] = i

    res = []
    count = 0
    visited = set()
    for r, c in positions:
        if (r, c) in visited:  # duplicate position
            res.append(count)  # do nothing
            continue
        visited.add((r, c))
        for ro, co in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            rn, cn = r + ro, c + co
            if (rn, cn) in visited:  # adjacent to previous position
                count -= union(table[(r, c)], table[(rn, cn)])
        count += 1
        res.append(count)
    return res


# union find, TC:O(N*alpha(N)), SC:O(N) N is length of positions(prevent double counting)
def numIslands22(m: int, n: int, positions: List[List[int]]) -> List[int]:
    parent, rank = {}, {}
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        x, y = find(x), find(y)
        if x == y:
            return 0
        if rank[x] < rank[y]:
            x, y = y, x
        parent[y] = x
        rank[x] += rank[x] == rank[y]
        return 1
    counts, count = [], 0
    for i, j in positions:
        if (i, j) not in parent:
            x = parent[x] = i, j
            rank[x] = 0
            count += 1
            for y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if y in parent:
                    count -= union(x, y)
            counts.append(count)
        else:
            counts.append(count)
    return counts