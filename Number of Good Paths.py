# https://leetcode.com/problems/number-of-good-paths/
# https://leetcode.com/problems/number-of-good-paths/solutions/2620680/python-union-find-solution/


import collections


# first thought, DFS(TLE), TC:O(), SC:O()
def numberOfGoodPaths(vals: List[int], edges: List[List[int]]) -> int:
    graph = collections.defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    def dfs(i, prev, end):
        if i == end:
            return True
        if vals[i] > vals[end]:
            return False

        for nei in graph[i]:
            if prev == nei:  # do not go back
                continue
            if dfs(nei, i, end):
                return True
        return False  # reach end

    memo = {}
    res = len(vals)
    for i, v in enumerate(vals):
        if v not in memo:
            memo[v] = [i]
        else:
            # do dfs from i to memo[v]
            for end in memo[v]:
                if dfs(i, -1, end):
                    res += 1
            memo[v].append(i)
    return res


# union find from the smallest edges, TC:O(N(alpha(N)+logN)), SC:O(N)
def numberOfGoodPaths2(vals: List[int], edges: List[List[int]]) -> int:
    # C(k,2) = k*(k-1)/2 for each max
    res = n = len(vals)
    parents = list(range(n))
    count = [collections.Counter({vals[i]: 1}) for i in range(n)]
    edges = sorted([max(vals[i], vals[j]),i,j] for i,j in edges)
    print(edges)
    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
    # [2,3,2,2,3], [[0,1],[0,2],[2,3],[2,4]]
    # 5(itself)+3(2's)+1(3's)
    for v,i,j in edges:
        fi, fj = find(i), find(j)
        cj, ci = count[fi][v], count[fj][v] # 0 and 1 if not the same value
        res += ci * cj
        parents[fj] = fi # union, fi(parent) and fj
        count[fi] = collections.Counter({v: ci + cj}) # update parent's counter
    return res