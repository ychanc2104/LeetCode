# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/

import collections


# first thought, union find, TC:O(N+M), SC:O(N)
def countPairs(n: int, edges: List[List[int]]) -> int:
    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        px, py = find(x), find(y)
        parents[px] = py

    parents = [i for i in range(n)]
    for a, b in edges:
        union(a, b)
    counter = collections.Counter([find(i) for i in range(n)])
    groups = list(counter.keys())
    n_groups = len(groups)
    res = 0
    accu = 0
    for i in range(n_groups):
        num = counter[groups[i]]
        res += counter[groups[i]] * (n - accu - num)
        accu += num

    return res